# American Option Pricing Using a Binomial Tree

This repository implements **American option pricing using the Cox–Ross–Rubinstein binomial tree model**, with an emphasis on **performance comparison between a naive loop-based approach and a NumPy-vectorized implementation**.

The project is designed to highlight how **early exercise decisions and vectorization** impact both option valuation and runtime performance.

---

## Overview

The binomial model discretizes time and models the underlying asset price using a **recombining tree**.

Unlike European options, American options can be exercised **at any point before maturity**. As a result, option values are computed using **risk-neutral valuation**, **backward induction**, and an **early exercise check at every node**.

Two implementations are provided:

- A **clear but slow** loop-based version
- A **fast and scalable** vectorized version using NumPy

Both methods price an **American option** and return the optimal exercise value at time zero.

---

## Implementations

### `american_slow_tree`

- Uses explicit Python loops
- Builds the asset price tree node by node
- Performs backward induction using nested loops
- Evaluates early exercise decisions at every node
- Easy to understand but inefficient for large `N`

### `american_fast_tree`

- Uses NumPy vectorization
- Computes terminal stock prices in one operation
- Vectorizes continuation value calculations
- Applies early exercise decisions using array operations
- Significantly faster and more scalable

Both implementations produce the same option price.

---

## Performance Benchmarking

A `timing` decorator is used to measure execution time for each method.

This makes the performance difference visible as the number of time steps increases while ensuring both implementations produce identical results.

---

## Key Assumptions

- Recombining binomial tree
- Constant risk-free interest rate
- No dividends
- American option (exercise allowed before maturity)
- No arbitrage pricing framework

---

## Purpose of This Project

This repository is useful for:

- Learning American option pricing from first principles
- Understanding backward induction clearly
- Seeing how early exercise affects option valuation
- Comparing **O(N²)** loop-based logic with optimized NumPy code
- Building intuition before moving to finite difference methods or Monte Carlo simulations

---

## Example Benchmark

The project can be executed for different tree sizes, such as:

```python
for N in [3, 1000]:
    american_fast_tree(K, T, S0, r, N, u, d, opttype='P')
    american_slow_tree(K, T, S0, r, N, u, d, opttype='P')
```
