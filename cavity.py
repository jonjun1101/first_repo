
# Import the Streamlit library
# im
port streamlit as st

# Title of the app
# st.title("Cavity")

# Header
#st.header("header")

# Input voltages
# max = st.number_input("Max voltage:", value=0.0)
# min = st.number_input("Min voltage:", value=0.0)
# offset = st.number_input("Offset voltage:", value=0.0)


# Perform the conversion
#contrast = ((max - offset) - (min - offset)) / ((max - offset) + (min - offset))

# Display the result
# st.write(f"The equivalent temperature in Fahrenheit is: **{contrast:.2f}**")

# Add an optional slider for fun
#st.subheader("Play around with the Celsius slider")
#celsius_slider = st.slider("Celsius", min_value=-100, max_value=100, value=0)
#st.write(f"Slider value in Fahrenheit: {celsius_slider * 9/5 + 32:.2f}°F")



import numpy as np
import matplotlib.pyplot as plt

def resonance_frequencies(cavity_length, mode_numbers, c=3e8):
    """
    Calculate the resonance frequencies of a cavity.
    
    Parameters:
    cavity_length (float): Length of the cavity in meters.
    mode_numbers (array): Array of mode numbers to compute frequencies.
    c (float): Speed of light in m/s (default is 3e8 m/s).
    
    Returns:
    frequencies (array): Resonance frequencies in Hz.
    """
    return mode_numbers * c / (2 * cavity_length)

# Define parameters
cavity_length = 1.0  # meters
mode_numbers = np.arange(1, 21)  # First 20 modes

# Compute resonance frequencies
frequencies = resonance_frequencies(cavity_length, mode_numbers)

# Plot the resonance frequencies
plt.figure(figsize=(8, 5))
plt.stem(mode_numbers, frequencies / 1e9, basefmt=" ")  # Convert to GHz for readability
plt.xlabel("Mode Number")
plt.ylabel("Resonance Frequency (GHz)")
plt.title(f"Resonance Frequencies for a {cavity_length} m Cavity")
plt.grid(True)
plt.show()
