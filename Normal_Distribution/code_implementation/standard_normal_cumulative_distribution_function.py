from probability_density_function import standard_normal_probability_density_function

# Cumulative Density Function using numerical integration (trapezoidal rule)
def standard_normal_cdf(x: float, num_steps=1000) -> float:
    if x < 0:
        # Use symmetry: Φ(-x) = 1 - Φ(x)
        return 1 - standard_normal_cdf(-x, num_steps)

    step =  x / num_steps
    area = 0.0
    for i in range(num_steps):
        xi = i * step
        xi1 = (i + 1) * step
        area += (standard_normal_probability_density_function(xi) + standard_normal_probability_density_function(xi1)) * step / 2
    return area



# Example usage
x_val = 1.0
print(f"PDF at x = {x_val}: {standard_normal_probability_density_function(x_val):.5f}")
print(f"CDF at x = {x_val}: {standard_normal_cdf(x_val):.5f}")