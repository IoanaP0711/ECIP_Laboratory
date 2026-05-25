import numpy as np
import matplotlib.pyplot as plt

# --- 1. Setup Data (From Task 1) ---
A, B, C = 1, 1, 1
steps = 30
np.random.seed(42)

x = np.zeros(steps)
u = np.ones(steps)
w = np.random.normal(0, 0.5, steps)

# Generate true state
for t in range(steps):
    if t < steps - 1:
        x[t+1] = A * x[t] + B * u[t] + w[t]

# --- 2. Exercise 2: Prediction Step ---
x_pred = np.zeros(steps)
# Initial condition \hat{x}(0|0) = 0 is met by np.zeros

for t in range(1, steps):
    # \hat{x}(t|t-1) = A * \hat{x}(t-1|t-1) + B * u(t)
    x_pred[t] = A * x_pred[t-1] + B * u[t]

# --- 3. Plotting ---
plt.figure(figsize=(10, 5))
plt.plot(range(steps), x, label='True State $x(t)$', marker='o', linestyle='-', color='blue')
plt.plot(range(steps), x_pred, label='Predicted State $\hat{x}(t|t-1)$', marker='x', linestyle='--', color='orange')
plt.title('Exercise 2: True State vs. Predicted State (No Update)')
plt.xlabel('Time Step (t)')
plt.ylabel('State Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()