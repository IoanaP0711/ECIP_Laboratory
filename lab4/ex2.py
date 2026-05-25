# #IOT Linear Model (Humidity vs Time)
# - Data: (time, humidity) = (1;40), (2;42), (3;45)
# - Model: y = ax + b
# - Build matrix A and vector y
# - Compute a and b using least squares


import numpy as np

# Data
x = np.array([1, 2, 3])
y = np.array([40, 42, 45])

# Build matrix A
A = np.vstack([x, np.ones(len(x))]).T

# Least squares solution
solution, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

a, b = solution

print("Matrix A:\n", A)
print("Vector y:\n", y)
print("\nSlope a =", a)
print("Intercept b =", b)