# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jn-Ye_cR_FC1gsbkmZdXpGsQCGFbsj12
"""

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('best_penguin_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Penguin Species Prediction")

# Collect user input features
island = st.selectbox('Island', ['Biscoe', 'Dream', 'Torgersen'])
bill_length_mm = st.slider('Bill Length (mm)', 30.0, 60.0)
bill_depth_mm = st.slider('Bill Depth (mm)', 13.0, 22.0)
flipper_length_mm = st.slider('Flipper Length (mm)', 170.0, 230.0)
body_mass_g = st.slider('Body Mass (g)', 2700.0, 6300.0)
sex = st.selectbox('Sex', ['Male', 'Female'])

# Prepare user input for prediction
user_input = np.array([bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g,
                       1 if island == 'Dream' else 0, 1 if island == 'Torgersen' else 0,
                       1 if sex == 'Male' else 0]).reshape(1, -1)

# Predict the species
prediction = model.predict(user_input)
species = ['Adelie', 'Chinstrap', 'Gentoo']
predicted_species = species[prediction[0]]

st.write(f"The predicted penguin species is: {predicted_species}")

