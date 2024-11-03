import streamlit as st
import BS_Calculations as bs_calc

st.write("""
# Black Scholes Pricing Model - Interactive Heatmap
""")

ticker_symbol = st.text_input("Enter a stock ticker:", "")

strike_price = st.number_input("Enter the strike price:", min_value=0.0, format="%.2f")
option_price = bs_calc.get_option_details(strike_price)