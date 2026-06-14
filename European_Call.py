# in here we will try to price a european model
import numpy as np
import time

#Compare between fast and slow
def time_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

S0 = 100  # intial stock price
K = 100  # strike price
TTE = 1  # time is always in years
r = 0.06  # risk free interest rate
N = 3  # number of time steps
u = 1.1  # upfactor
d = 1/u  # down factor ensuring recombining tree
optionType = 'C'  # can be C or P

@time_wrapper
def binomial_tree_slow(K, TTE, S0, r, N, u, d, optiontype='C'):
    # computing constants
    dt = TTE/N
    # risk neutral parameter
    q = (np.exp(r*dt)-d)/(u-d)
    discountFactor = np.exp(-r*dt)

    # Intialize asset prices at maturity - time step N
    S = np.zeros(N+1)
    # at the bottom of the tree
    S[0] = S0*d**N
    for j in range(1, N+1):
        S[j] = S[j-1]*u/d

    # Intialize option values at maturity
    C = np.zeros(N+1)
    # Computing payoffs for the european call option
    for j in range(0, N+1):
        C[j] = max(0, S[j]-K)

    # Step backwards through the tree
    for i in np.arange(N, 0, -1):
        for j in range(0, i):
            C[j] = discountFactor*(q*C[j+1] + (1-q)*C[j])

    return C[0]  # discounted risk neutral expected value of the option payoff


#vectorizing functions using numpy array
@time_wrapper
def binomial_tree_fast(K, TTE, S0, r, N, u, d, optiontype='C'):
    # computing constants
    dt = TTE/N
    # risk neutral parameter
    q = (np.exp(r*dt)-d)/(u-d)
    discountFactor = np.exp(-r*dt)

    # Intialize asset prices at maturity - time step N
    C = S0 * d**(np.arange(N, -1, -1)) * u**(np.arange(0, N+1, 1))

    # Intialize option values at maturity
    C = np.maximum(C-K, np.zeros(N+1))

    # Step backwards through the tree
    for i in np.arange(N, 0, -1):
        C = discountFactor * ( q * C[1:i+1] + (1-q) * C[0:i])

    return C[0]  # discounted risk neutral expected value of the option payoff

