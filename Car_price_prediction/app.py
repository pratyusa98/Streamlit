import numpy as np
import pickle
import pandas as pd
import streamlit as st 


pickle_in = open("car price.pkl","rb")
price_finder=pickle.load(pickle_in)

def main():
	st.title('Car_Price_Prediction')

	year = st.text_input('year of purchase','Type Here')
	Present_Price = st.text_input("Present_Price(in lacs)","Type Here")
	Kms_Driven = st.text_input("Kms_Driven","Type Here")
	Fuel_Type = st.selectbox("Fuel_Type",("Petrol","Diesel"))

	if Fuel_Type=="Petrol":
		Fuel_Type=0
	else:
		Fuel_Type=1

	
	Seller_Type = st.selectbox("Seller_Type",("Dealer","Individual"))
	if Seller_Type=="Dealer":
		Seller_Type=0
	else:
		Seller_Type=1

	Transmission = st.selectbox("Transmission",("Manual","Automatic"))
	if Transmission=="Manual":
		Transmission=0
	else:
		Transmission=1

	Owner = st.text_input("Owner","Type Here")

	data = [[year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]]
	
	if st.button("Predict"):
		prediction =  price_finder.predict(data)

		st.success('The output is {} lacks'.format(prediction[0]))




if __name__=='__main__':
    main()