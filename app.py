import streamlit as st
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("customer_churn_ann_model.h5")

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Set page config
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

# Title
st.title("Customer Churn Prediction using ANN")
st.write("Enter customer details below to predict whether the customer will churn or stay.")

# Form for user input
with st.form("churn_form"):
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)
    num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=2)

    has_cr_card_text = st.selectbox("Has Credit Card", ["No", "Yes"])
    is_active_member_text = st.selectbox("Is Active Member", ["No", "Yes"])
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Female", "Male"])

    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

    submit_button = st.form_submit_button("Predict Churn")

if submit_button:
    # Convert Yes/No fields to 0/1
    has_cr_card = 1 if has_cr_card_text == "Yes" else 0
    is_active_member = 1 if is_active_member_text == "Yes" else 0

    # Convert categorical variables to encoded values
    geography_germany = 1 if geography == "Germany" else 0
    geography_spain = 1 if geography == "Spain" else 0
    gender_male = 1 if gender == "Male" else 0

    # Create input dataframe with same column order as training data
    input_data = pd.DataFrame([{
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_of_products,
        "HasCrCard": has_cr_card,
        "IsActiveMember": is_active_member,
        "EstimatedSalary": estimated_salary,
        "Geography_Germany": geography_germany,
        "Geography_Spain": geography_spain,
        "Gender_Male": gender_male
    }])

    # Scale input data
    input_data_scaled = scaler.transform(input_data)

    # Predict churn probability
    prediction = model.predict(input_data_scaled, verbose=0)
    churn_prob = float(prediction[0][0])

    # Display result
st.subheader("Prediction Result")
st.write(f"Churn Probability: {churn_prob * 100:.2f}%")

if churn_prob > 0.5:
    st.write("The model predicts that this customer has a high chance of churning.")
    st.error("Final Prediction: Customer will churn")
else:
    st.write("The model predicts that this customer is likely to stay with the bank.")
    st.success("Final Prediction: Customer will stay")