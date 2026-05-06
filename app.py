import streamlit as st

st.title("Streamlit Demo App")
st.markdown("This is a simple Streamlit app to demonstrate its capabilities.")

username = st.text_input("Enter your username:")

st.slider("Select your age:", 0, 100, 25)
st.checkbox("Subscribe to newsletter")
st.button("Submit")
st.balloons()

st.write(f"Hello, {username}! Welcome to the Streamlit demo app.")