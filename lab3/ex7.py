# sensor measurement simulation
# simulate value x=10
# generate measurements with y=x+noise
# plot measurement distribution

import numpy as np
import matplotlib.pyplot as plt

# True value
x = 10

# Generate noise and measurements
n = 1000
noise = np.random.normal(0, 1, n)   # Gaussian noise: mean=0, std=1
y = x + noise

# Print basic statistics
print("True value x =", x)
print("Sample mean of measurements =", np.mean(y))
print("Sample variance of measurements =", np.var(y))

# Plot histogram of measurements
plt.figure(figsize=(8, 5))
plt.hist(y, bins=30, edgecolor='black')
plt.axvline(x, linestyle='--', label=f"True value = {x}")
plt.title("Distribution of Sensor Measurements")
plt.xlabel("Measured value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()