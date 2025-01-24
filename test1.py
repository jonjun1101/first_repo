# Import the Streamlit library
import streamlit as st

# Title of the app
st.title("Calculate Homodyne Contrast")

# Header
#st.header("header")

# Input voltages
maximum = st.number_input("Max voltage:", value=0.0)
minimum = st.number_input("Min voltage:", value=0.0)
offset = st.number_input("Offset voltage:", value=0.0)


# Perform the conversion
contrast = ((max - offset) + (min - offset)) / ((max - offset) - (min - offset))

# Display the result
st.write(f"The equivalent temperature in Fahrenheit is: **{contrast:.2f}°F**")

# Add an optional slider for fun
#st.subheader("Play around with the Celsius slider")
#celsius_slider = st.slider("Celsius", min_value=-100, max_value=100, value=0)
#st.write(f"Slider value in Fahrenheit: {celsius_slider * 9/5 + 32:.2f}°F")
