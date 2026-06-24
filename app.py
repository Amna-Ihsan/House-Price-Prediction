import joblib 
import streamlit as st
import pandas as pd

# load the model
model = joblib.load("linear_regression_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("House Price Prediction")

square_footage = st.number_input("Square Footage", min_value=0)
num_of_bedrooms = st.selectbox("Number of Bedrooms",[1,2,3,4,5])
num_of_bathrooms = st.selectbox("Number of Bathrooms", [1,2,3])
year_built = st.number_input("Year Built",min_value=1800,max_value=2026,step=1)
lot_size = st.number_input("Lot Size", min_value=0.0)
garage_size = st.selectbox("Garage Size", [0,1,2])
neighborhood_quality = st.slider("Neighborhood Quality", 1, 10, 5)

if st.button("Predict House Price"):
    input_data = pd.DataFrame([{
        "Square_Footage": square_footage,
        "Num_Bedrooms": num_of_bedrooms,
        "Num_Bathrooms": num_of_bathrooms,
        "Year_Built": year_built,
        "Lot_Size": lot_size,
        "Garage_Size": garage_size,
        "Neighborhood_Quality": neighborhood_quality
    }])


    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    st.success(f"Predicted Selling Price: ${prediction[0]:.2f}")
    