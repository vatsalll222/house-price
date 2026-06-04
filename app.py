import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction")

st.divider()

st.write("Please enter the following details to predict the house price")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=0)
living_area = st.number_input("Living Area", min_value=0, value=2000)
condition = st.number_input("Condition", min_value=0, value=3)
numberofschools = st.number_input("Number of Schools nearby", min_value=0, value=0)
distancefromairport = st.number_input("Distance from Airport", min_value=0, value=0)
numberoffloors = st.number_input("Number of Floors", min_value=0, value=0)
st.divider()

X = [[bedrooms, bathrooms, living_area, condition, numberofschools, distancefromairport, numberoffloors]]

predictbutton = st.button("Predict")

if predictbutton:
    st.balloons()
    X_array = np.array(X)
    prediction = model.predict(X_array)
    st.write(f"The predicted house price is: {prediction[0]:.2f}")
else:
    st.write("Please fill in all the details to predict the house price")