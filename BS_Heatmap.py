import streamlit as st
import BS_Calculations as bs_calc

st.write("""
# Black Scholes Pricing Model - Interactive Heatmap
""")

ticker_symbol = st.text_input("Enter a stock ticker:", "")
