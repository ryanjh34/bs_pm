import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Split Layout Example", layout="wide")

# Create a sidebar for inputs
st.sidebar.title("Black-Scholes Pricing Model")
stock_ticker = st.sidebar.text_input("Stock Ticker")
input_number = st.sidebar.number_input("Enter a number:", min_value=0)

# Main area
st.markdown('<div class="main-background">', unsafe_allow_html=True)
st.title("Options Price - Interactive Heatmap")
st.write("You entered: ", stock_ticker)
st.write("Number entered: ", input_number)
