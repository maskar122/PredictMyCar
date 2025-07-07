import streamlit as st
import numpy as np
import pickle

# تحميل النموذج المدرب
with open('C:/Users/LAP-STORE/Desktop/Amit/p1/car_prediction/random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

st.title("Car Price Prediction")


# المستخدم يدخل كل الـ 10 features بنفس الترتيب اللي اتدرب عليه النموذج
power = st.number_input("Power (bhp)", min_value=20.0, max_value=600.0)
engine = st.number_input("Engine (CC)", min_value=500.0, max_value=5000.0)
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
year = st.number_input("Year", min_value=1990, max_value=2025)
mileage = st.number_input("Mileage (kmpl)", min_value=5.0, max_value=40.0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=300000)
location = st.selectbox("Location", ['Mumbai', 'Pune', 'Chennai', 'Coimbatore',
                                     'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata',
                                     'Delhi', 'Bangalore', 'Ahmedabad'])

# تحويل القيم النصية إلى أرقام كما تم أثناء التدريب
transmission_map = {"Manual": 0, "Automatic": 1}
fuel_map = {"CNG": 0, "Diesel": 1, "Petrol": 2, "LPG": 3, "Electric": 4}
location_map = {'Mumbai': 7, 'Pune': 9, 'Chennai': 1, 'Coimbatore': 2,
                'Hyderabad': 5, 'Jaipur': 6, 'Kochi': 3, 'Kolkata': 4,
                'Delhi': 0, 'Bangalore': 8, 'Ahmedabad': 10}

input_data = np.array([[power,
                        engine,
                        transmission_map[transmission],
                        year,
                        mileage,
                        fuel_map[fuel_type],
                        km_driven,
                        location_map[location],
                        0,  # Seats
                        0]]) # Owner_Type

if st.button("Predict Price"):
    prediction = rf_model.predict(input_data)[0]
    st.success(f"Predicted Price: ${prediction:.2f}")
