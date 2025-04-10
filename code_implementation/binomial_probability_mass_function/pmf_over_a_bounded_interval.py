# Probability Over a Bounded Interval:
from pmf import binomial_pmf

def binomial_prob_between(n: int, a: int, b: int, p: float) -> float:
    return sum(binomial_pmf(n, x, p) for x in range(a, b + 1))


n = 10
p = 0.5
a = 3
b = 6

# P(3 ≤ X ≤ 6)
print("P(3 ≤ X ≤ 6):", binomial_prob_between(n, a, b, p))