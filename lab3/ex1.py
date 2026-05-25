import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers between 0 and 1
random_numbers = np.random.rand(1000)

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(random_numbers, bins=30, edgecolor='black')
plt.title("Histogram of 1000 Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()