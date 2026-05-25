# estimate true Value
# compute average of noisy measurements
# compare estimate with true value
# discuss estimation error 

import numpy as np
import matplotlib.pyplot as plt

# True value
x = 10

# Generate noisy measurements
n = 1000
noise = np.random.normal(0, 1, n)   # mean = 0, std = 1
y = x + noise

# Estimate true value using average
x_est = np.mean(y)

# Estimation error
error = x_est - x

# Print results
print("True value:", x)
print("Estimated value (average of measurements):", x_est)
print("Estimation error:", error)
print("Absolute error:", abs(error))

# Plot histogram of measurements
plt.figure(figsize=(8, 5))
plt.hist(y, bins=30, edgecolor='black')
plt.axvline(x, linestyle='--', label=f"True value = {x}")
plt.axvline(x_est, linestyle='--', label=f"Estimated value = {x_est:.4f}")
plt.title("Noisy Measurements and Estimated True Value")
plt.xlabel("Measured value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()