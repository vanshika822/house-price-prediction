import streamlit as st
import numpy as np
import pandas as pd
import os
# from model import predict_price
import requests


st.set_page_config(page_title="house dashboard")
st.title("House Dashboard")
st.markdown('---')

file_path = os.path.join(os.path.dirname(__file__),"House_Price.csv")
house=pd.read_csv(file_path)    


st.subheader("House Price Prediction ")

col1, col2 = st.columns(2)
with col1:
    area = st.number_input("Select Area", min_value=0, max_value=10000, step=100, key="p1")
with col2:
    bedrooms = st.number_input("Select Bedrooms", min_value=0, max_value=10, step=1, key="p2")
with col1:
    bathrooms = st.number_input("Select Bathrooms", min_value=0, max_value=10, step=1, key="p3")
with col2:
    house_age = st.number_input("Select House Age", min_value=0, max_value=100, step=1, key="p4")   

with col1:
    distance = st.number_input("Select Distance from City", min_value=0, max_value=100, step=1, key="p5")
with col2:
    parking = st.number_input("Select Parking Slots", min_value=0, max_value=10, step=1, key="p6")

floor = st.selectbox("Select Floor", sorted(house['Floor'].unique()), key="p7")
if st.button("Predict Price"):

    payload = {
    "area": float(area),
    "bedrooms": int(bedrooms),
    "bathrooms": int(bathrooms),
    "house_age": int(house_age),
    "distance_city": float(distance),
    "parking": int(parking),
    "floor": int(floor)
}

    response = requests.post(
    "https://house-price-prediction-a2v6.onrender.com/predict",
    json=payload
)
    # st.write("status code:",response.status_code)
    # st.write("response text:",response.text)

    result = response.json()["predicted_price"]
        # result = predict_price(
        #     area,
        #     bedrooms,
        #     bathrooms,
        #     house_age,
        #     distance,
        #     parking,
        #     floor
        # )

    st.success(f"Estimated House Price : ₹ { result :.2f} Lakhs")   
    st.balloons()


# fig,ax=plt.subplots()
# house['Bedrooms'].value_counts().plot(kind='bar',color='grey',ax=ax)
# ax.set_title("Bedroom Count Distribution")
# ax.set_xlabel("No. Of Bedrooms")
# ax.set_ylabel("No.Of Houses")
# st.pyplot(fig)
