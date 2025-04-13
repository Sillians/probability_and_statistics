import  math

"""
The standard normal distribution is a special case of the normal distribution with:

Mean = 0
Standard Deviation = 1
"""

# Probability Density Function of the Standard Normal Distribution
def standard_normal_probability_density_function(x: float) -> float:
    return (1 / math.sqrt(2 * math.pi) * math.exp(-0.5 * x**2))

