# app.py

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input data from form
        input_data = [float(x) for x in request.form.values()]
        final_input = np.array(input_data).reshape(1, -1)

        # Make prediction
        prediction = model.predict(final_input)[0]

        if prediction == 1:
            result = "The person is likely to have diabetes."
        else:
            result = "The person is unlikely to have diabetes."

        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)