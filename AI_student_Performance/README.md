# AI Student Performance Predictor

## 1. Project Overview

AI Student Performance Predictor is a web application that uses a machine learning model to predict a student's performance based on academic and personal factors.

## 2. Problem Statement

The purpose of this project is to predict student performance using factors such as study hours, attendance, previous marks, assignment marks, sleep hours, and practice questions.

## 3. Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- SQLite
- Joblib

## 4. Features

- Student data input
- AI-based performance prediction
- Machine learning model
- Prediction result
- Prediction history
- Simple and responsive interface

## 5. Dataset

The dataset contains student-related features such as:

- Study hours
- Attendance
- Previous marks
- Assignment marks
- Sleep hours
- Practice questions

The target variable is student performance.

## 6. Machine Learning Model

Random Forest Classifier is used to predict student performance.

The dataset is divided into training and testing data.

## 7. Data Preprocessing

The input features are separated from the target variable.

The dataset is divided into training and testing sets before training the model.

## 8. Model Evaluation

The trained model is evaluated using accuracy score on the test dataset.

## 9. Application Architecture

Student → Frontend → Flask Backend → ML Model → Prediction → Frontend

## 10. How to Run

Install the required packages:

```bash
pip install -r requirements.txt