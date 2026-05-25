import numpy as np
import matplotlib.pyplot as plt

# Data: time vs energy
time = np.array([1, 2, 3, 4, 5])
energy = np.array([2.1, 2.9, 3.8, 4.2, 5.1])

# Build matrix A for the linear model y = ax + b
A = np.vstack([time, np.ones(len(time))]).T

# Compute least squares solution
solution, residuals, rank, s = np.linalg.lstsq(A, energy, rcond=None)
a, b = solution

# Compute fitted values
energy_pred = A @ solution

# Print results
print("Matrix A:")
print(A)
print("\nEnergy vector y:")
print(energy)

print("\nSlope (consumption rate):", a)
print("Intercept:", b)

# Plot measured data and fitted line
plt.figure(figsize=(8, 5))
plt.scatter(time, energy, label="Measured data")
plt.plot(time, energy_pred, label="Fitted line")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.title("Smart Home Energy Consumption Model")
plt.legend()
plt.grid(True)
plt.show()

# Interpretation
print("\nInterpretation:")
print(f"The slope a = {a:.2f} represents the energy consumption rate.")
print(f"This means the energy increases by about {a:.2f} units per unit of time.")
print(f"The intercept b = {b:.2f} is the estimated energy value at time 0.")
