import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("svm.sav", "rb") as f:
    model = pickle.load(f)

st.title("🩺  Diabetes Prediction using SVM")
st.write("Enter the patient details below to predict whether they may have diabetes.")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=2)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=95)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=120)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=1000, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=18.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.6)
age = st.number_input("Age", min_value=1, max_value=120, value=55)

input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]

if st.button("Predict"):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("🩸 **The patient is Diabetic**")
    else:
        st.success("💚 **The patient is Not Diabetic**")

