from BS_Variables import get_black_scholes_inputs
from scipy.stats import norm
import numpy as np
import math

# gather initial inputs
ticker_symbol = input("Enter a stock ticker: ").upper()
print("")
black_scholes_params = get_black_scholes_inputs(ticker_symbol)

# gather variables
S = black_scholes_params['S']
K = black_scholes_params['K']
T = black_scholes_params['T']
r = black_scholes_params['r']
sigma = black_scholes_params['sigma']
e = math.e

# cummulative normal distribution
def N(x):
    return norm.cdf(x)

# probability factors
d1 = (np.log(S/K) + T * (r + (sigma**2/2)))/(sigma * np.sqrt(T)) # multiplies current stock price
d2 = (np.log(S/K) + T * (r - (sigma**2/2)))/(sigma * np.sqrt(T)) # multiplies discounted exercise payment

C = S * N(d1) - K * math.pow(e,-r*T) * N(d2)

print(f"{C:.3f}")

