from pmf import binomial_pmf

# Example
n = 7  # number of trials
p = 0.5  # probability of success
k = 4   # desired number of successes

probability = binomial_pmf(n, k, p)
print(f"P(X = {k}) for Bin({n}, {p}) = {probability:.5f}")