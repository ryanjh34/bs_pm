import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Split Layout Example", layout="wide")

risk_free_rate = 4.25

# Create a sidebar for inputs
st.sidebar.title("Black-Scholes Pricing Model")
stock_ticker = st.sidebar.text_input("Stock Ticker")
strike_price = st.sidebar.number_input("Strike Price", min_value=0)
expiration_date = st.sidebar.text_input("Expiration Date (YYYY-MM-DD)", min_value=0)
st.sidebar.text(f"Current Risk-Free Rate: {risk_free_rate:.2%}")

# Main area
st.markdown('<div class="main-background">', unsafe_allow_html=True)
st.title("Options Price - Interactive Heatmap")
st.write("You entered: ", stock_ticker)
st.write("Number entered: ", strike_price)
