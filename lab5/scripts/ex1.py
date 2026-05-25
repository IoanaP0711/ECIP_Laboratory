import numpy as np
import matplotlib.pyplot as plt

# --- System Parameters ---
A = 1
B = 1
C = 1
steps = 30  # Total number of time steps

# Pre-allocate arrays for state, measurement, and control input
x = np.zeros(steps)
y = np.zeros(steps)
u = np.ones(steps)  # u(t) = 1 for all time steps

# --- Noise Setup ---
# We use a small standard deviation for the "small random noise" requirement
std_dev_w = 0.5  # Standard deviation for process noise w(t)
std_dev_v = 0.5  # Standard deviation for measurement noise v(t)

# Generate Gaussian (normal) random noise for all steps
w = np.random.normal(0, std_dev_w, steps)
v = np.random.normal(0, std_dev_v, steps)

# --- Simulation ---
# Initial state x(0) = 0 is already handled by np.zeros

for t in range(steps):
    # 2. Generate the noisy measurements: y(t) = Cx(t) + v(t)
    y[t] = C * x[t] + v[t]
    
    # 1. Generate the true state (calculate the next state): x(t+1) = Ax(t) + Bu(t) + w(t)
    # We only update up to the second-to-last step to avoid index out-of-bounds
    if t < steps - 1:
        x[t+1] = A * x[t] + B * u[t] + w[t]

# --- 3. Plotting ---
plt.figure(figsize=(10, 6))

# Plot true state
plt.plot(range(steps), x, label='True State $x(t)$', marker='o', linestyle='-', color='blue')

# Plot measured output
plt.plot(range(steps), y, label='Noisy Measurement $y(t)$', marker='x', linestyle='--', color='red')

# Formatting the graph
plt.title('Simple Linear Dynamic System Simulation')
plt.xlabel('Time Step (t)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()