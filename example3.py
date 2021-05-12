import streamlit as st

# Text/Title
st.title('How to receive user input and process them with streamlit?')

# Receiving User Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")

# Text Area
message = st.text_area("Enter Your message","Type Here..")

# Date Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())


# Time
the_time = st.time_input("The time is",datetime.time())


if st.button("Submit"):
	firstname = firstname.title()
	message = message.title()

	st.success(firstname)
	st.info(message)
	st.info(today)