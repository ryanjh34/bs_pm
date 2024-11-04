import streamlit as st

# Apply custom CSS for left alignment
st.markdown("""
    <style>
    .stTextInput label {
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.write("# Black Scholes Pricing Model - Interactive Heatmap")

# Left-aligned input field for ticker symbol
ticker_symbol = st.text_input("Enter a stock ticker:", "")
