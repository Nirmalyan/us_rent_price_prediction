import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
import numpy as np

laundry_dict = {'laundry in bldg': 1, 'no laundry on site': 2,
                'laundry on site': 3, 'w/d hookups': 4, 'NA': 5, 'w/d in unit': 6}
parking_dict = {'off-street parking': 1, 'carport': 2, 'street parking': 3,
                'no parking': 4, 'attached garage': 5, 'valet parking': 6, 'NA': 7, 'detached garage': 8}
housing_dict = {'in-law': 1, 'assisted living': 2, 'apartment': 3, 'townhouse': 4, 'cottage/cabin': 5,
                'flat': 6, 'loft': 7, 'house': 8, 'condo': 9, 'manufactured': 10, 'duplex': 11, 'land': 12}
binary_option = {'Yes': 1, 'No': 0}

st.write(":house: **House Rent Price Prediction**")
sqft = st.text_input("Enter required sqft of the house", value="")
bed = st.selectbox('How many beds', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
bath = st.selectbox('How many bathroom', (1, 2, 3, 4, 5, 6, 7))
parking = st.selectbox('Parking type', ('off-street parking', 'carport', 'street parking',
                       'no parking', 'attached garage', 'valet parking', 'NA', 'detached garage'))
laundry = st.selectbox('Laundry type', ('laundry in bldg', 'no laundry on site',
                       'laundry on site', 'w/d hookups', 'NA', 'w/d in unit'))
housing = st.selectbox('Select Housing Type', ('in-law', 'assisted living', 'apartment', 'townhouse',
                       'cottage/cabin', 'flat', 'loft', 'house', 'condo', 'manufactured', 'duplex', 'land'))

col1, col2, col3 = st.columns(3)
col11, col21, col31 = st.columns(3)

with col1:
    cats = st.radio('Cats?', ("Yes", "No"))
with col2:
    dogs = st.radio('Dogs?', ("Yes", "No"))
with col3:
    smoking = st.radio('Smoking?', ("Yes", "No"))
with col11:
    wheelchair = st.radio('Wheelchair?', ("Yes", "No"))
with col21:
    evcharge = st.radio('EVCharging?', ("Yes", "No"))
with col31:
    furnish = st.radio('Furnished?', ("Yes", "No"))

if st.button('Get Rent Estimate'):
    loaded_model = pickle.load(open('prediction_model.sav', 'rb'))
    model_input = [int(sqft), bed, float(bath), binary_option[cats], binary_option[dogs], binary_option[smoking], binary_option[
        wheelchair], binary_option[evcharge], binary_option[furnish], laundry_dict[laundry], parking_dict[parking], housing_dict[housing]]
    model_input = np.array(model_input).reshape(1, -1)
    result = loaded_model.predict(model_input)
    st.write(f"Estimated Price ${float(result)}")
