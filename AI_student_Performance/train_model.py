import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# 1. Load dataset
data = pd.read_csv("dataset/students.csv")


# 2. Select input features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_marks",
        "sleep_hours",
        "practice_questions"
    ]
]


# 3. Select target
y = data["performance"]


# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 6. Train model
model.fit(X_train, y_train)


# 7. Make predictions
y_pred = model.predict(X_test)


# 8. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)


# 9. Save trained model
joblib.dump(model, "model/model.pkl")

print("Model saved successfully!")