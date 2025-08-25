# --- 1. Import Libraries ---
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# --- 2. Create Flask App ---
# The __name__ variable gets the name of the current Python script.
app = Flask(__name__)

# --- 3. Load The Model ---
# Load the trained model from the file.
model = joblib.load('house_price_model.joblib')

# --- 4. Create a Prediction API Endpoint ---
# @app.route defines the URL path. '/predict' is the endpoint we'll use.
# methods=['POST'] means this endpoint only accepts POST requests.
@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives house data in a POST request, uses the loaded model
    to make a prediction, and returns the prediction as JSON.
    """
    # Get the JSON data sent from the frontend
    json_data = request.get_json()

    # Create a pandas DataFrame from the JSON data
    # The [0] is because we're sending a single record in a list
    df = pd.DataFrame(json_data)

    # --- 5. Feature Engineering (Must match the notebook!) ---
    # It's crucial that the features here are created in the exact
    # same way as they were in the training notebook.
    current_year = 2024 # Use the same year as in your notebook
    df['HouseAge'] = current_year - df['YearBuilt']

    # Define the final features the model expects, in the correct order
    model_features = [
        'OverallQual',
        'GrLivArea',
        'GarageCars',
        'TotalBsmtSF',
        'FullBath',
        'HouseAge'
    ]

    # Ensure the DataFrame has the columns in the correct order
    df_final = df[model_features]

    # --- 6. Make Prediction ---
    # Use the model to predict the log-transformed price
    prediction_log = model.predict(df_final)

    # Reverse the log transformation to get the actual price
    prediction = np.expm1(prediction_log)

    # --- 7. Return the Prediction ---
    # Return the prediction in a JSON format
    return jsonify({'prediction': prediction[0]})


# --- 8. Run The App ---
# This line allows you to run the app directly from the command line
if __name__ == '__main__':
    # host='0.0.0.0' makes the app accessible from your local network
    # port=5000 is the default port for Flask
    app.run(host='0.0.0.0', port=5000, debug=True)