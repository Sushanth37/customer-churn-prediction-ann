# Customer Churn Prediction using ANN

This project predicts whether a bank customer will churn or stay using an Artificial Neural Network built with TensorFlow and Keras.

## Objective
The objective of this project is to predict whether a customer will leave the bank or stay based on customer-related features such as credit score, age, balance, number of products, geography, gender, and activity status.

## Tools and Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow
- Keras

## Dataset
The project uses the `Churn_Modelling.csv` dataset, which contains customer details and the target column `Exited`.

- `Exited = 1` means the customer left the bank
- `Exited = 0` means the customer stayed with the bank

## Project Workflow
1. Import the required libraries
2. Load the dataset
3. Check dataset information and missing values
4. Drop unnecessary columns
5. Encode categorical columns
6. Split the data into features and target
7. Perform train-test split
8. Apply feature scaling
9. Build the ANN model
10. Compile and train the model
11. Predict on test data
12. Evaluate the model using accuracy, confusion matrix, and classification report
13. Predict churn for new customer data
14. Save the trained model and scaler

## Model Architecture
The Artificial Neural Network consists of:
- Input layer with 11 features
- First hidden layer with 11 neurons and sigmoid activation
- Second hidden layer with 11 neurons and sigmoid activation
- Output layer with 1 neuron and sigmoid activation

## Evaluation Metrics
The model is evaluated using:
- Accuracy Score
- Confusion Matrix
- Classification Report

## Example Output
Churn Probability: 0.83  
Final Prediction: Customer will churn

or

Churn Probability: 0.21  
Final Prediction: Customer will stay

## Files in this Repository
- `ChurnProject.ipynb` - main Jupyter notebook
- `Churn_Modelling.csv` - dataset
- `customer_churn_ann_model.h5` - saved ANN model
- `scaler.pkl` - saved feature scaler

## Conclusion
This project successfully predicts customer churn using an ANN model built with TensorFlow and Keras. It demonstrates the complete machine learning workflow from data preprocessing to model training, evaluation, and prediction on new customer inputs.
