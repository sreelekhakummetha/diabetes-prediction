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
└── index.html # Frontend form for user input

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


 
