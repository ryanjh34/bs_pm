import streamlit as st

# Header
st.write("# Black Scholes Pricing Model - Interactive Heatmap")

# Create two columns with specified width
col1, col2 = st.columns(2)  # Adjust the ratios as needed

# Content in the left column
with col1:
# Left-aligned input field for ticker symbol
    ticker_symbol = st.text_input("Enter a stock ticker:", "")

# Content in the right column (optional)
with col2:
    st.write("This is the right column, which can be used for other content.")
