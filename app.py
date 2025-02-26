import streamlit as st
import json
from streamlit_lottie import st_lottie

# Page Configuration
st.set_page_config(page_title="🎨 Dynamic  Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS Styling for Colorful UI
st.markdown("""
    <style>
    .stApp {
        background-color:rgb(7, 30, 51);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #ff6600;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
        transition: all 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #cc5200;
        transform: scale(1.05);
    }
    .result-box {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to Load Lottie Animations
def load_lottie_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# Load Animation
lottie_conversion = load_lottie_file("conversion_animation.json")

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371}
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

def currency_converter(value, from_unit, to_unit):
    currency_rates = {"USD": 1, "EUR": 0.85, "GBP": 0.75, "INR": 74.50, "PKR": 280.50}
    return value * (currency_rates[to_unit] / currency_rates[from_unit])

# Streamlit UI
st.title("🌍 **Dynamic & Colorful Unit Converter App**")
st.markdown("<h3 style='color: #ff6600;'>Convert different units easily with a vibrant UI! 🌟</h3>", unsafe_allow_html=True)

# Display Animation
if lottie_conversion:
    st_lottie(lottie_conversion, height=200, key="conversion")

# Sidebar
conversion_type = st.sidebar.selectbox("**🔀 Select Conversion Type**", ["Length", "Weight", "Temperature", "Currency"])

value = st.number_input("📌 **Enter Value**", min_value=0.0, format="%.2f")

if value:
    if conversion_type == "Length":
        from_unit = st.selectbox("📏 **From Unit**", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
        to_unit = st.selectbox("📏 **To Unit**", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
        result = length_converter(value, from_unit, to_unit)
        st.markdown("<h3 style='color: #007BFF;'>📏 Length Conversion</h3>", unsafe_allow_html=True)
    elif conversion_type == "Weight":
        from_unit = st.selectbox("⚖️ **From Unit**", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        to_unit = st.selectbox("⚖️ **To Unit**", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        result = weight_converter(value, from_unit, to_unit)
        st.markdown("<h3 style='color: #007BFF;'>⚖️ Weight Conversion</h3>", unsafe_allow_html=True)
    elif conversion_type == "Temperature":
        from_unit = st.selectbox("🌡️ **From Unit**", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("🌡️ **To Unit**", ["Celsius", "Fahrenheit", "Kelvin"])
        result = temperature_converter(value, from_unit, to_unit)
        st.markdown("<h3 style='color: #007BFF;'>🌡️ Temperature Conversion</h3>", unsafe_allow_html=True)
    elif conversion_type == "Currency":
        from_unit = st.selectbox("💰 **From Currency**", ["USD", "EUR", "GBP", "INR", "PKR"])
        to_unit = st.selectbox("💰 **To Currency**", ["USD", "EUR", "GBP", "INR", "PKR"])
        result = currency_converter(value, from_unit, to_unit)
        st.markdown("<h3 style='color: #007BFF;'>💰 Currency Conversion</h3>", unsafe_allow_html=True)

    # Display Converted Result
    st.markdown(f"<div class='result-box'>✅ Converted Value: {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
