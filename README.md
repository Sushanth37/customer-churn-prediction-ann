# Customer Churn Prediction using ANN (Deep Learning)

A deep learning-based project that predicts whether a bank customer is likely to churn or stay using an Artificial Neural Network (ANN). The project includes both model training in Jupyter Notebook and a Streamlit web application for real-time prediction.

## Project Overview

Customer churn prediction is important for banks because retaining existing customers is often more valuable than acquiring new ones. In this project, customer details are used to predict the probability of churn.

The project workflow includes:

- data preprocessing
- feature encoding
- feature scaling
- ANN model training
- model saving
- frontend development using Streamlit

## Features

- Predicts whether a customer will churn or stay
- Displays churn probability
- Takes user input through a simple Streamlit interface
- Uses saved trained ANN model and scaler
- Converts categorical inputs into numerical format before prediction

## Technologies Used

- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Project Structure

- `ChurnProject.ipynb` - notebook for preprocessing, training, and evaluation
- `app.py` - Streamlit frontend for prediction
- `customer_churn_ann_model.h5` - saved ANN model
- `scaler.pkl` - saved scaler
- `Churn_Modelling.csv` - dataset
- `requirements.txt` - required Python packages
- `README.md` - project documentation

## How It Works

1. User enters customer details in the Streamlit app
2. Categorical values are converted into numerical features
3. Input data is arranged in the same format used during training
4. The saved scaler transforms the input values
5. The ANN model predicts churn probability
6. The app displays the final prediction

## How to Run the Project

```bash
git clone https://github.com/Sushanth37/customer-churn-prediction-ann.git
cd customer-churn-prediction-ann
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```
