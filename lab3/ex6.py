# generate gaussian noise with different variances
# plot and compare solutions
# discuss uncertainty


import numpy as np
import matplotlib.pyplot as plt

# Fix seed for reproducibility
np.random.seed(42)

# Generate Gaussian noise with mean = 0 and different variances
n = 1000

noise1 = np.random.normal(0, np.sqrt(0.2), n)   # variance = 0.2
noise2 = np.random.normal(0, np.sqrt(1.0), n)   # variance = 1.0
noise3 = np.random.normal(0, np.sqrt(3.0), n)   # variance = 3.0

# Print sample statistics
print("Noise 1: variance = 0.2")
print("Sample mean:", np.mean(noise1))
print("Sample variance:", np.var(noise1))
print()

print("Noise 2: variance = 1.0")
print("Sample mean:", np.mean(noise2))
print("Sample variance:", np.var(noise2))
print()

print("Noise 3: variance = 3.0")
print("Sample mean:", np.mean(noise3))
print("Sample variance:", np.var(noise3))

# Plot histograms separately
plt.figure(figsize=(8, 5))
plt.hist(noise1, bins=30, edgecolor='black')
plt.title("Gaussian Noise with Variance 0.2")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(noise2, bins=30, edgecolor='black')
plt.title("Gaussian Noise with Variance 1.0")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(noise3, bins=30, edgecolor='black')
plt.title("Gaussian Noise with Variance 3.0")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Compare all on one figure
plt.figure(figsize=(10, 5))
plt.hist(noise1, bins=30, alpha=0.5, edgecolor='black', label='Var = 0.2')
plt.hist(noise2, bins=30, alpha=0.5, edgecolor='black', label='Var = 1.0')
plt.hist(noise3, bins=30, alpha=0.5, edgecolor='black', label='Var = 3.0')
plt.title("Comparison of Gaussian Noise with Different Variances")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()