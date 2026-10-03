from flask import Flask, render_template, request
import joblib
import sqlite3
import os

app = Flask(__name__)

# Load trained model
model = joblib.load("model/model.pkl")

# Create database folder
os.makedirs("database", exist_ok=True)


# Create database
def create_database():
    connection = sqlite3.connect("database/predictions.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_hours REAL,
            attendance REAL,
            previous_marks REAL,
            assignment_marks REAL,
            sleep_hours REAL,
            practice_questions INTEGER,
            prediction TEXT
        )
    """)

    connection.commit()
    connection.close()


create_database()


# Get prediction history
def get_history():
    connection = sqlite3.connect("database/predictions.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT study_hours,
               attendance,
               previous_marks,
               assignment_marks,
               sleep_hours,
               practice_questions,
               prediction
        FROM predictions
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


# Home page
@app.route("/")
def home():
    history = get_history()

    return render_template(
        "index.html",
        history=history
    )


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_marks = float(request.form["previous_marks"])
    assignment_marks = float(request.form["assignment_marks"])
    sleep_hours = float(request.form["sleep_hours"])
    practice_questions = int(request.form["practice_questions"])

    input_data = [[
        study_hours,
        attendance,
        previous_marks,
        assignment_marks,
        sleep_hours,
        practice_questions
    ]]

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Save to database
    connection = sqlite3.connect("database/predictions.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (
            study_hours,
            attendance,
            previous_marks,
            assignment_marks,
            sleep_hours,
            practice_questions,
            prediction
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        study_hours,
        attendance,
        previous_marks,
        assignment_marks,
        sleep_hours,
        practice_questions,
        prediction
    ))

    connection.commit()
    connection.close()

    # Get updated history
    history = get_history()

    return render_template(
        "index.html",
        prediction=prediction,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)