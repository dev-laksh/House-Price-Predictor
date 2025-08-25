House Price Predictor 🏡
Welcome to the House Price Predictor, a comprehensive, full-stack web application designed to estimate property values using a powerful machine learning model. This project serves as a practical demonstration of an end-to-end data science workflow, showcasing the journey from raw data to a live, interactive user application. The core of this project is a RandomForestRegressor model trained on the renowned Ames Housing dataset from Kaggle.

The entire process, from initial data exploration and rigorous feature engineering in a Jupyter Notebook to the final deployment of the model via a Flask-powered REST API, is documented and implemented. The front-end, built with modern and clean HTML and Tailwind CSS, provides an intuitive interface for users to input key housing characteristics—such as living area, build quality, and garage size—and receive an instant price prediction.

✨ Key Features
Interactive Web Interface: A responsive and visually appealing front-end allows users to easily input property details. The interface is designed for simplicity and provides immediate feedback with the estimated price.

Robust Machine Learning Backend: A lightweight yet powerful backend built with Flask serves the pre-trained scikit-learn model. It exposes a clean REST API endpoint that handles incoming data, processes it, and returns predictions efficiently.

Real-time Prediction Engine: The application delivers predictions on the fly. When a user submits the form, a POST request containing the feature data is sent to the Flask API, which leverages the trained model to return an accurate, real-time valuation.

Complete Data Science Workflow: This repository is not just an application but a case study. It covers essential data science stages, including data cleaning, exploratory data analysis (EDA), feature engineering, model training and evaluation, and finally, productionalization with a web server.

🛠️ Tech Stack
Backend: Python, Flask, scikit-learn, Pandas, NumPy

Frontend: HTML, Tailwind CSS, JavaScript

ML Model: RandomForestRegressor

Deployment: The model is serialized using joblib and served locally.

🚀 How to Run
Clone the repository:

git clone https://github.com/dev-laksh/house-price-predictor.git
cd house-price-predictor

Install dependencies:

pip install -r requirements.txt

Run the Flask API:

python app.py

Open the application:
Open the index.html file in your web browser to start making predictions!
