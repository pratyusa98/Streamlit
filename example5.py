import streamlit as st

st.subheader("Displaying Progressbars,Spinners and Balloons")

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(15):
    my_bar.progress(p + 1)


# Spinner
with st.spinner("Waiting .."):
     time.sleep(5)
     st.success("Finished!")

# Balloons
st.balloons()