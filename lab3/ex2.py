# simulate a random variable X ~ Uniform(0,1)
# plot histogram
# interpret distribution shape

import numpy as np
import matplotlib.pyplot as plt

# Simulate a random variable X ~ Uniform(0,1)
x = np.random.uniform(0, 1, 1000)

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(x, bins=30, edgecolor='black')
plt.title("Histogram of X ~ Uniform(0,1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()