# Task 1 - IOT Temperature Sensor Calibration
# - Sensor Readings: y = [21, 22, 23, 24]
# - Assume true temperature is constant x
# - Task: compute x that best fits data
# - Interpret x as calibrated temperature


import numpy as np

# Sensor readings
y = np.array([21, 22, 23, 24])

# Estimate x (best constant fit = mean)
x = np.mean(y)

print("Calibrated temperature x =", x)