import streamlit as st
import pickle
import numpy as np
import base64
from io import BytesIO


def load_model():
    with open('mega_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


model = load_model()

def show_predict_page():
    st.title('Auto 1985 Predictor')
    st.write('''We need some information to predict the car price''')

    enginesize = st.slider('engine-size', 50, 350)
    curb = st.slider('curb-weight', 1000, 5000)
    highway_mpg = st.slider('highway-mpg', 10, 60)
    horsepower = st.slider('horsepower', 30, 300)
    width = st.slider('width', 50, 100)

    X = np.array([[enginesize, curb, horsepower, highway_mpg, width]])
    price = model.predict(X)
    st.subheader(f"The estimated price is ${price[0]:.2f}")