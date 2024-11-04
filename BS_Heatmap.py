import streamlit as st

st.columns(spec, *, gap="small", vertical_alignment="top")

# Header
st.write("# Black Scholes Pricing Model - Interactive Heatmap")

# Left-aligned input field for ticker symbol
ticker_symbol = st.text_input("Enter a stock ticker:", "")
