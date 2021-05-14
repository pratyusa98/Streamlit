import streamlit as st

st.subheader('Showing Sidebars')

st.text('With streamlit you can create sidebars with ease. For now you can use any of the functions except st.write,st.echo,st.code with the sidebar method.')

# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")

# Normal Function
def run_fxn():
    return range(100)

st.write(run_fxn())

# To Improve Performance/Speed via caching
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())