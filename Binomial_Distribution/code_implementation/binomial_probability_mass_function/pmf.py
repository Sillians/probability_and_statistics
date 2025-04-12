# Binomial Probability Mass Function (PMF)

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))

def binomial_pmf(n: int, k: int, p: float) -> float:
    combinatorics = combination(n, k)
    prob_success = (p ** k)
    prob_failures = (1 - p) ** (n - k)

    pmf = combinatorics * prob_success * prob_failures
    return pmf