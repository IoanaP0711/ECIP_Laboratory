# convariance
# generate two correlated variables
# compute convariance
# interpret relationship

import numpy as np
import matplotlib.pyplot as plt

# Generate data
np.random.seed(42)
n = 1000

# First variable
x = np.random.normal(0, 1, n)

# Second variable correlated with x
y = 2 * x + np.random.normal(0, 0.5, n)

# Compute covariance
cov_matrix = np.cov(x, y)
cov_xy = cov_matrix[0, 1]

# Print results
print("Covariance matrix:\n", cov_matrix)
print("Covariance between x and y:", cov_xy)

# Scatter plot
plt.figure(figsize=(6, 6))
plt.scatter(x, y, alpha=0.5)
plt.title("Scatter Plot of Correlated Variables")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()