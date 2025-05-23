# 🩺 Diabetes Prediction Web App 🩺

A web application built with **Flask** and **Machine Learning** that predicts whether a person is likely to have diabetes based on medical diagnostic measurements.

---

## 📌 Project Overview

This project uses a **Machine Learning classification model** trained on the Pima Indians Diabetes Database to predict diabetes. The app allows users to input patient health data through a simple web form and get instant predictions.

---

## 📊 Technologies Used

- **Python 3**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **HTML / CSS (for frontend)**
- **Joblib** (for model serialization)

---

## 📁 Project Structure

diabetes-prediction-flask/
│
├── app.py # Flask web app
├── prediction.py # Model training and saving script
├── diabetes_model.pkl # Saved trained ML model 
├── README.md # Project info and instructions
└── templates/
└── index.html
|__ screenshots/
|___ homepage.png
|___ prediction.png

# Frontend form for user input

---

## ⚙️ How to Run the Project Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sreelekhakummetha/diabetes-prediction-flask.git
   cd diabetes-prediction-flask
   
2. **create virtual environment
   python -m venv venv
   
3.Activate virtual environment
.\venv\Scripts\activate

4.install requirements

5.Run falsk app
python app.py

6.Open the App
Visit http://127.0.0.1:5000/ in your web browser.


📊 Input Features

The app uses the following health parameters for prediction:

Pregnancies — Number of times pregnant

Glucose — Plasma glucose concentration

BloodPressure — Diastolic blood pressure (mm Hg)

SkinThickness — Triceps skinfold thickness (mm)

Insulin — 2-Hour serum insulin (mu U/ml)

BMI — Body mass index (weight in kg/(height in m)^2)

DiabetesPedigreeFunction — Diabetes pedigree function (hereditary factor)

Age — Age in years

📜 License

This project is open-source and free to use under the MIT License.

DEMO

## 📸 Screenshots

### 🔹 Home Page
screenshots/homepage.png

### 🔹 Prediction Result
screenshots/prediction.png







 
