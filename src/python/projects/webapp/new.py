import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Slider input
number = st.slider("Pick a number:", min_value=1, max_value=100, value=50)

# Display the output
if st.button("Submit"):
    st.write(f"Hello, {name}! You picked the number {number}.")