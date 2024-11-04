# packages
import numpy as np
from datetime import datetime
import pytz
import yfinance as yf
from fredapi import Fred
from scipy.stats import norm
import math
import streamlit as st

# Set up the Fred API key
fred = Fred(api_key='721f0a5be3b2e6f7f8651124afd64889')

# Set the page configuration
st.set_page_config(page_title="Black-Scholes Calculator", layout="wide")

# Function to get the current stock price (S)
def get_current_stock_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    stock_price = stock.history(period="1d")['Close'].iloc[0]
    return stock_price

# Function to get option chain and select a strike price (K) and expiration date
def get_option_details(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    expiration_dates = stock.options  # get available expiration dates
    expiration_choice = st.selectbox("Choose an expiration date:", expiration_dates)  # user selects expiration date
    opt_chain = stock.option_chain(expiration_choice)  # use the chosen expiration date
    available_strikes = opt_chain.calls['strike'].tolist()  # get available strike prices
    strike_input = st.selectbox("Select a strike price:", available_strikes)  # user selects strike price
    return strike_input, expiration_choice  # return strike price and expiration date

# Function to calculate time to expiration (T) in years
def calculate_time_to_expiration(expiration_date):
    current_date = datetime.now(pytz.timezone('America/Chicago'))  # current time in CST
    expiration_datetime = datetime.strptime(expiration_date, "%Y-%m-%d")  # convert to datetime
    # Set expiration time to 3:00 PM CST
    expiration_datetime = expiration_datetime.replace(hour=15, minute=0, second=0)
    # Localize expiration date to CST
    expiration_datetime = pytz.timezone('America/Chicago').localize(expiration_datetime)
    # Calculate the difference in time and convert to years
    time_to_expiration = (expiration_datetime - current_date).total_seconds() / (365 * 24 * 3600)
    return time_to_expiration

# Function to get risk-free interest rate (r) from the most recent 1-year Treasury yield
def get_risk_free_rate():
    risk_free_rate_series = fred.get_series('DGS1')  # Get the full series
    risk_free_rate = risk_free_rate_series.dropna().iloc[-1]  # Get the most recent non-NaN value
    return risk_free_rate / 100  # Convert from percentage to decimal

# Function to calculate stock price volatility (sigma)
def calculate_volatility(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    historical_data = stock.history(period="1y")  # get 1 year of historical data
    historical_data['Returns'] = historical_data['Close'].pct_change()  # calculate daily returns
    volatility = np.std(historical_data['Returns']) * np.sqrt(252)  # annualized volatility
    return volatility

# Gather inputs and return variables
def get_black_scholes_inputs(ticker_symbol):
    S = get_current_stock_price(ticker_symbol)  # current stock price
    K, expiration_date = get_option_details(ticker_symbol)  # option strike price and expiration date
    T = calculate_time_to_expiration(expiration_date)  # time to expiration (in years)
    r = get_risk_free_rate()  # risk-free interest rate
    sigma = calculate_volatility(ticker_symbol)  # volatility of stock returns
    return {
        'S': S,
        'K': K,
        'T': T,
        'r': r,
        'sigma': sigma,
        'expiration_date': expiration_date
    }

# Function to calculate the Black-Scholes call option price
def calculate_call_option_price(S, K, T, r, sigma):
    e = math.e
    d1 = (np.log(S/K) + T * (r + (sigma**2/2))) / (sigma * np.sqrt(T))  # d1 calculation
    d2 = d1 - sigma * np.sqrt(T)  # d2 calculation
    C = S * norm.cdf(d1) - K * math.pow(e, -r * T) * norm.cdf(d2)  # call price formula
    return C

# Sidebar for inputs
st.sidebar.title("Black-Scholes Inputs")
ticker_symbol = st.sidebar.text_input("Enter a stock ticker:").upper()

if ticker_symbol:  # Proceed only if a ticker symbol is entered
    black_scholes_params = get_black_scholes_inputs(ticker_symbol)

    # Gather variables
    S = black_scholes_params['S']
    K = black_scholes_params['K']
    T = black_scholes_params['T']
    r = black_scholes_params['r']
    sigma = black_scholes_params['sigma']

    # Display results in the main area
    st.markdown('<div class="main-background">', unsafe_allow_html=True)
    st.title("Black-Scholes Call Option Price")
    st.write("Current Stock Price (S): ${:.2f}".format(S))
    st.write("Option Strike Price (K): ${:.2f}".format(K))
    st.write("Time to Expiration (T): {:.2f} years or {:.0f} days".format(T, T * 365))
    st.write("Risk-Free Rate (r): {:.2%}".format(r))
    st.write("Volatility (sigma): {:.2%}".format(sigma))
    st.write("Expiration Date: {}".format(black_scholes_params['expiration_date']))

    # Calculate and display the call option price
    call_price = calculate_call_option_price(S, K, T, r, sigma)
    st.write("Calculated Call Option Price: ${:.2f}".format(call_price))
    st.markdown('</div>', unsafe_allow_html=True)
