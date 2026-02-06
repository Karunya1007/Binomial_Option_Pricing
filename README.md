# European Option Pricing Using a Binomial Tree

This repository implements **European option pricing using the Cox–Ross–Rubinstein binomial tree model**, with an emphasis on **performance comparison between a naive loop-based approach and a NumPy-vectorized implementation**.

The project is designed to highlight how **algorithmic structure and vectorization** impact runtime while producing the same theoretical option price.

---

## Overview

The binomial model discretizes time and models the underlying asset price using a **recombining tree**.  
Option prices are computed using **risk-neutral valuation** and **backward induction**.

Two implementations are provided:
- A **clear but slow** loop-based version
- A **fast and scalable** vectorized version using NumPy

Both methods price a **European Call option** and return the discounted expected payoff at time zero.

---

## Model Parameters

- Initial stock price: `S0`
- Strike price: `K`
- Time to expiry (years): `TTE`
- Risk-free interest rate: `r`
- Number of time steps: `N`
- Up factor: `u`
- Down factor: `d = 1/u` (ensures recombining tree)
- Option type: European Call
- Risk-neutral probability: q = (e^(rt) - d)/(u - d)

---

## Implementations

### `binomial_tree_slow`
- Uses explicit Python loops
- Builds the asset price tree node by node
- Performs backward induction using nested loops
- Easy to understand but inefficient for large `N`

### `binomial_tree_fast`
- Uses NumPy vectorization
- Computes terminal asset prices in one operation
- Collapses backward induction into array operations
- Significantly faster and more scalable

Both implementations produce the same option price.

---

## Performance Benchmarking

A `time_wrapper` decorator is used to measure execution time for each method.  
This makes the performance difference visible as the number of time steps increases.

---

## Key Assumptions

- Recombining binomial tree
- Constant risk-free interest rate
- No dividends
- European option (exercise only at maturity)
- No arbitrage pricing framework

---

## Purpose of This Project

This repository is useful for:
- Learning binomial option pricing from first principles
- Understanding backward induction clearly
- Seeing why recombining trees are important
- Comparing **O(N²)** loop-based logic with optimized NumPy code
- Building intuition before moving to Black–Scholes or Monte Carlo methods

---
