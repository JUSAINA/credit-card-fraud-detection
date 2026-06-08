import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Credit Card Fraud Detection")

features = []

for i in range(30):
    value = st.number_input(f"Feature {i}")
    features.append(value)

if st.button("Predict"):
    
    prediction = model.predict([features])

    if prediction[0] == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Genuine Transaction")