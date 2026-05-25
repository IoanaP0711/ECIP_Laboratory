#  compute the variance of generated data
# analyze spread around mean
# compare datasets with different variances

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Dataset 1: X ~ Uniform(0,1)
# -----------------------------
x1 = np.random.uniform(0, 1, 1000)

mean1 = np.mean(x1)
var1 = np.var(x1)

# Theoretical variance for Uniform(0,1)
theoretical_var1 = (1 - 0) ** 2 / 12

print("DATASET 1: Uniform(0,1)")
print("Sample mean:", mean1)
print("Sample variance:", var1)
print("Theoretical variance:", theoretical_var1)
print()

# -----------------------------
# Dataset 2: Y ~ Uniform(0,2)
# -----------------------------
x2 = np.random.uniform(0, 2, 1000)

mean2 = np.mean(x2)
var2 = np.var(x2)

# Theoretical variance for Uniform(0,2)
theoretical_var2 = (2 - 0) ** 2 / 12

print("DATASET 2: Uniform(0,2)")
print("Sample mean:", mean2)
print("Sample variance:", var2)
print("Theoretical variance:", theoretical_var2)

# -----------------------------
# Plot histograms
# -----------------------------
plt.figure(figsize=(10, 5))

plt.hist(x1, bins=30, alpha=0.6, edgecolor='black', label='Uniform(0,1)')
plt.hist(x2, bins=30, alpha=0.6, edgecolor='black', label='Uniform(0,2)')

plt.axvline(mean1, linestyle='--', label=f'Mean X1 = {mean1:.3f}')
plt.axvline(mean2, linestyle='--', label=f'Mean X2 = {mean2:.3f}')

plt.title("Comparison of Two Uniform Distributions")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()