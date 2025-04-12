# Probability Over an Unbounded Interval
from pmf import binomial_pmf

# summing the PMF from k to n:
def binomial_prob_geq(n: int, k: int, p: float):
    return sum(binomial_pmf(n, x, p) for x in range(k, n + 1))


n = 10
p = 0.5
k = 7

# P(X >= 7)
print("P(X ≥ 7):", binomial_prob_geq(n, k, p))