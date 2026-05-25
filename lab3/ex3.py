# # compute sample mean of generated data
# compare with theoretical mean
# discuss interpretation of expectation

import numpy as np
import matplotlib.pyplot as plt

# Simulate X ~ Uniform(0,1)
x = np.random.uniform(0, 1, 1000)

# Compute sample mean
sample_mean = np.mean(x)

# Theoretical mean for Uniform(0,1)
theoretical_mean = 0.5

# Print results
print("Sample mean:", sample_mean)
print("Theoretical mean:", theoretical_mean)

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(x, bins=30, edgecolor='black')
plt.axvline(sample_mean, linestyle='--', label=f"Sample mean = {sample_mean:.4f}")
plt.axvline(theoretical_mean, linestyle='--', label=f"Theoretical mean = {theoretical_mean:.4f}")
plt.title("Histogram of X ~ Uniform(0,1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()