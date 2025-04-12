# Using the Complement Rule:
from pmf import binomial_pmf

def binomial_prob_geq_complement(n: int, k: int, p: float):
    return round(1 - sum(binomial_pmf(n, x, p) for x in range(k)), 4)


n = 10
p = 0.6
k = 8

# P(X ≥ 8) using complement
print("P(X ≥ 8) using complement:", binomial_prob_geq_complement(n, k, p))