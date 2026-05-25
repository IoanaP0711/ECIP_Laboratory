import numpy as np
import matplotlib.pyplot as plt


A, B, C = 1, 1, 1
steps = 30
np.random.seed(42)

x = np.zeros(steps)
y = np.zeros(steps)
u = np.ones(steps)
w = np.random.normal(0, 0.5, steps)
v = np.random.normal(0, 0.5, steps)

# Generate true state and measurements
for t in range(steps):
    y[t] = C * x[t] + v[t]
    if t < steps - 1:
        x[t+1] = A * x[t] + B * u[t] + w[t]

# --- 2. Prerequisite: Prediction Step (From Ex 2) ---
x_pred = np.zeros(steps)
for t in range(1, steps):
    x_pred[t] = A * x_pred[t-1] + B * u[t]

# --- 3. Exercise 3: Innovation ---
innovation = np.zeros(steps)

for t in range(steps):
    # Innovation = y(t) - C * \hat{x}(t|t-1)
    innovation[t] = y[t] - C * x_pred[t]

# --- 4. Plotting ---
plt.figure(figsize=(10, 5))
plt.plot(range(steps), innovation, label='Innovation', marker='s', linestyle='-', color='purple')
plt.axhline(0, color='black', linestyle='--', linewidth=1) # Reference line at 0
plt.title('Exercise 3: Innovation over Time')
plt.xlabel('Time Step (t)')
plt.ylabel('Innovation Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()