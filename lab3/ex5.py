# generate gaussian random variable with mean=0 std=1
# plot histogram
# compare with uniform distribution

import numpy as np
import matplotlib.pyplot as plt

# Generate random variables
uniform_data = np.random.uniform(0, 1, 1000)   # Uniform(0,1)
gaussian_data = np.random.normal(0, 1, 1000)   # Gaussian(mean=0, std=1)

# Print means and variances
print("Uniform(0,1)")
print("Sample mean:", np.mean(uniform_data))
print("Sample variance:", np.var(uniform_data))
print()

print("Gaussian(0,1)")
print("Sample mean:", np.mean(gaussian_data))
print("Sample variance:", np.var(gaussian_data))

# Plot histogram for Gaussian
plt.figure(figsize=(8, 5))
plt.hist(gaussian_data, bins=30, edgecolor='black')
plt.title("Histogram of Gaussian Random Variable N(0,1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Compare both distributions
plt.figure(figsize=(10, 5))
plt.hist(uniform_data, bins=30, alpha=0.6, edgecolor='black', label='Uniform(0,1)')
plt.hist(gaussian_data, bins=30, alpha=0.6, edgecolor='black', label='Gaussian N(0,1)')
plt.title("Comparison: Uniform vs Gaussian Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()