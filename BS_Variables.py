# packages
import numpy as np
from datetime import datetime, timedelta
import pytz
import yfinance as yf
from fredapi import fred

fred = Fred(api_key='721f0a5be3b2e6f7f8651124afd64889')

# get current stock price (S)
def get_current_stock_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    stock_price = stock.history(period="1d")['Close'].iloc[0]
    return stock_price

# get option chain and select a strike price (K) and expiration date
def get_option_details(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    expiration_dates = stock.options  # get available expiration dates

    # List available expiration dates
    print("Available expiration dates: [{}]".format(", ".join(expiration_dates)))

    expiration_choice = int(input("Choose an expiration date (1-{}): ".format(len(expiration_dates)))) - 1
    print("")
    expiration_date = expiration_dates[expiration_choice]

    opt_chain = stock.option_chain(expiration_date)  # use the chosen expiration date
    available_strikes = opt_chain.calls['strike'].tolist()  # get available strike prices

    strike_input = float(input("Enter a strike price: "))  # user input for strike price
    print("")
    return strike_input, expiration_date  # return strike price and expiration date

# calculate time to expiration (T) in years
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

# set a risk-free interest rate (r) from most recent 1-year Treasury yield
def get_risk_free_rate():
    risk_free_rate_series = fred.get_series('DGS1')  # Get the full series
    risk_free_rate = risk_free_rate_series.dropna().iloc[-1]  # Get the most recent non-NaN value
    return risk_free_rate / 100  # Convert from percentage to decimal

# calculate stock price volatility (sigma)
def calculate_volatility(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    historical_data = stock.history(period="1y")  # get 1 year of historical data
    historical_data['Returns'] = historical_data['Close'].pct_change()  # calculate daily returns
    volatility = np.std(historical_data['Returns']) * np.sqrt(252)  # annualized volatility
    return volatility

# gather inputs and returns variables
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

# testing inputs & parameters
# ticker_symbol = input("Enter a stock ticker: ").upper()
# print("")
# black_scholes_params = get_black_scholes_inputs(ticker_symbol)
# print("Black-Scholes Inputs:")
# print(f"Current Stock Price (S): {black_scholes_params['S']:.2f}")
# print(f"Option Strike Price (K): {black_scholes_params['K']:.2f}")
# print(f"Time to Expiration (T): {black_scholes_params['T']} years or {(black_scholes_params['T']*365):.0f} days")
# print(f"Risk-Free Rate (r): {black_scholes_params['r']:.2%}")
# print(f"Volatility (sigma): {black_scholes_params['sigma']:.2%}")
# print(f"Expiration Date: {black_scholes_params['expiration_date']}")
