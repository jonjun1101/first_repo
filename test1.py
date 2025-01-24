# Import the Streamlit library
import streamlit as st

# Title of the app
st.title("Temperature Converter")

# Header
st.header("Convert Celsius to Fahrenheit")

# Input widget to get Celsius temperature from the user
celsius = st.number_input("Enter temperature in Celsius:", min_value=-100.0, max_value=100.0, value=0.0)

# Perform the conversion
fahrenheit = celsius * 9/5 + 32

# Display the result
st.write(f"The equivalent temperature in Fahrenheit is: **{fahrenheit:.2f}°F**")

# Add an optional slider for fun
st.subheader("Play around with the Celsius slider")
celsius_slider = st.slider("Celsius", min_value=-100, max_value=100, value=0)
st.write(f"Slider value in Fahrenheit: {celsius_slider * 9/5 + 32:.2f}°F")
