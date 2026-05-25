# #IoT prediction  error
# use results from last problem
# compute predicted values Ax 
# compute residuals r = y - Ax
# compute squared error 

import numpy as np

# Original data
x = np.array([1, 2, 3])
y = np.array([40, 42, 45])

# Build matrix A
A = np.vstack([x, np.ones(len(x))]).T

# Previously computed parameters
a = 2.5
b = 37.6666666667

# Parameter vector
theta = np.array([a, b])

# Predicted values Ax
y_pred = A @ theta

# Residuals r = y - Ax
r = y - y_pred

# Squared error
squared_error = np.sum(r**2)

print("Predicted values (Ax):", y_pred)
print("Residuals (r):", r)
print("Squared error:", squared_error)