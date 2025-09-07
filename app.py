import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("insurance_model.pkl")

st.title("Travel Insurance Prediction App")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", min_value=1000, max_value=1000000, value=50000)
family = st.number_input("Family Members", min_value=1, max_value=20, value=3)
chronic = st.selectbox("Chronic Diseases", [0, 1])
employment = st.selectbox("Employment Type", ["Government Sector", "Private Sector/Self-Employed"])
graduate = st.selectbox("Graduate or Not", ["Yes", "No"])
flyer = st.selectbox("Frequent Flyer", ["Yes", "No"])
abroad = st.selectbox("Ever Travelled Abroad", ["Yes", "No"])

# Make a dataframe from user input
input_data = pd.DataFrame({
    "Age": [age],
    "AnnualIncome": [income],
    "FamilyMembers": [family],
    "ChronicDiseases": [chronic],
    "Employment Type": [employment],
    "GraduateOrNot": [graduate],
    "FrequentFlyer": [flyer],
    "EverTravelledAbroad": [abroad]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ This person is likely to BUY Travel Insurance")
    else:
        st.error("❌ This person is NOT likely to buy Travel Insurance")
