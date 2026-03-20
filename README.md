# Customer Churn Prediction using ANN

This project predicts whether a bank customer will churn or stay using an Artificial Neural Network (ANN).

## Project Overview

This project was first developed in Jupyter Notebook for model training and then extended using Streamlit to create a simple frontend application for prediction.

The user enters customer details such as:

- Credit Score
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Member Status
- Geography
- Gender
- Estimated Salary

The application preprocesses the input, scales it using the saved scaler, and then uses the trained ANN model to predict the churn probability.

## Technologies Used

- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Files in the Project

- `ChurnProject.ipynb` - notebook used for data preprocessing, training, and evaluation
- `app.py` - Streamlit frontend application
- `customer_churn_ann_model.h5` - saved trained ANN model
- `scaler.pkl` - saved scaler object
- `Churn_Modelling.csv` - dataset used for training/testing

## How to Run the Project

1. Clone the repository
2. Open the project folder in VS Code
3. Create and activate a virtual environment
4. Install required packages
5. Run the Streamlit app

### Commands

```bash
git clone https://github.com/Sushanth37/customer-churn-prediction-ann.git
cd customer-churn-prediction-ann
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```
