import numpy as np
import matplotlib.pyplot as plt

# --- 1. Base Setup & Data Generation ---
A, B, C, I = 1, 1, 1, 1
steps = 30
np.random.seed(42)

x_true = np.zeros(steps)
y_meas = np.zeros(steps)
u = np.ones(steps)

# We generate one fixed dataset to ensure a fair comparison.
# We'll use the "baseline" Q and R values from Ex 4 for the true noise generation.
true_Q = 0.01
true_R = 0.5
w = np.random.normal(0, np.sqrt(true_Q), steps)
v = np.random.normal(0, np.sqrt(true_R), steps)

for t in range(steps):
    y_meas[t] = C * x_true[t] + v[t]
    if t < steps - 1:
        x_true[t+1] = A * x_true[t] + B * u[t] + w[t]

# --- 2. Exercise 6: Varying Q ---
Q_values = [0.0001, 0.01, 1]
R_fixed = 0.5  # Keep R constant for this exercise

# Dictionary to store the estimates for plotting
estimates = {}

for Q in Q_values:
    x_hat = np.zeros(steps)
    P = np.zeros(steps)
    x_hat[0] = 0
    P[0] = 1.0
    
    for t in range(1, steps):
        # Prediction
        x_pred = A * x_hat[t-1] + B * u[t]
        P_pred = A * P[t-1] * A + Q
        
        # Update
        S = C * P_pred * C + R_fixed
        K = (P_pred * C) / S
        x_hat[t] = x_pred + K * (y_meas[t] - C * x_pred)
        P[t] = (I - K * C) * P_pred
        
    estimates[Q] = x_hat

# --- 3. Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(range(steps), x_true, label='True State $x(t)$', color='black', linewidth=2, linestyle='--')
# Optional: Plot measurements lightly to see the noise
# plt.plot(range(steps), y_meas, label='Measurements', marker='x', linestyle='', color='gray', alpha=0.5)

colors = ['blue', 'orange', 'red']
markers = ['o', 's', '^']

for i, Q in enumerate(Q_values):
    plt.plot(range(steps), estimates[Q], label=f'Estimate (Q = {Q})', color=colors[i], marker=markers[i], markersize=5)

plt.title('Exercise 6: Effect of varying Process Noise Covariance $Q$')
plt.xlabel('Time Step (t)')
plt.ylabel('State Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()