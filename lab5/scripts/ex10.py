import numpy as np
import matplotlib.pyplot as plt

# --- 1. Filter & System Parameters ---
A, B, C, I = 1, 1, 1, 1
Q = 0.01  
R = 0.5   
L = 0.5   # Control gain from the prompt
steps = 40
np.random.seed(42)

# Pre-allocate arrays
x = np.zeros(steps)
y = np.zeros(steps)
u = np.zeros(steps)
x_hat = np.zeros(steps)
P = np.zeros(steps)

# Initial conditions (set x(0) to 5 so we can watch the controller regulate it)
x[0] = 5.0
x_hat[0] = 0.0 # The filter doesn't know the initial state is 5
P[0] = 1.0

# Generate noise sequences
w = np.random.normal(0, np.sqrt(Q), steps)
v = np.random.normal(0, np.sqrt(R), steps)

# --- 2. Closed-Loop Simulation ---
for t in range(steps):
    # 1. Take Measurement of the current true state
    y[t] = C * x[t] + v[t]

    # 2. Kalman Filter Update (Calculate \hat{x}(t|t))
    if t > 0:
        # Prediction using the previous state and previous control input
        x_pred = A * x_hat[t-1] + B * u[t-1]
        P_pred = A * P[t-1] * A + Q
        
        # Measurement Update
        S = C * P_pred * C + R
        K = (P_pred * C) / S
        x_hat[t] = x_pred + K * (y[t] - C * x_pred)
        P[t] = (I - K * C) * P_pred

    # 3. Apply Control Law: u(t) = -L * \hat{x}(t|t)
    u[t] = -L * x_hat[t]

    # 4. Advance the True System to t+1
    if t < steps - 1:
        x[t+1] = A * x[t] + B * u[t] + w[t]

# --- 3. Plotting ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot State
ax1.plot(range(steps), x, label='True State $x(t)$', color='blue', marker='o', linestyle='-')
ax1.plot(range(steps), x_hat, label='Estimated State $\hat{x}(t|t)$', color='orange', marker='x', linestyle='--')
ax1.set_title('Closed Loop State Regulation')
ax1.set_ylabel('State Value')
ax1.legend()
ax1.grid(True)

# Plot Control Signal
ax2.plot(range(steps), u, label='Control Signal $u(t)$', color='green', marker='s', linestyle='-')
ax2.set_title('Control Signal over Time')
ax2.set_xlabel('Time Step (t)')
ax2.set_ylabel('Control Input')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()