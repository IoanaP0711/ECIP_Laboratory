import numpy as np
import matplotlib.pyplot as plt

# --- 1. Filter Parameters (From previous exercises) ---
A, C, I = 1, 1, 1
Q = 0.01  # Process noise covariance
R = 0.5   # Measurement noise covariance
steps = 30

# Arrays to store covariances
P_pred = np.zeros(steps)  # P(t|t-1): Predicted covariance
P_upd = np.zeros(steps)   # P(t|t): Updated covariance

# Initial condition
P_upd[0] = 1.0
P_pred[0] = np.nan # Undefined at t=0 for plotting purposes

# --- 2. Covariance Calculation Loop ---
for t in range(1, steps):
    # 1. Predict Covariance: P(t|t-1) = A * P(t-1|t-1) * A^T + Q
    P_pred[t] = A * P_upd[t-1] * A + Q
    
    # Calculate Kalman Gain
    S = C * P_pred[t] * C + R
    K = (P_pred[t] * C) / S
    
    # 2. Update Covariance: P(t|t) = (I - K*C) * P(t|t-1)
    P_upd[t] = (I - K * C) * P_pred[t]

# --- 3. Plotting ---
plt.figure(figsize=(10, 6))

# Plot from t=1 onwards since P(0| -1) is not explicitly defined in our loop
t_range = range(1, steps)

plt.plot(t_range, P_pred[1:], label='Predicted Covariance $P(t|t-1)$', color='orange', marker='o', linestyle='--')
plt.plot(t_range, P_upd[1:], label='Updated Covariance $P(t|t)$', color='blue', marker='s', linestyle='-')

plt.title('Exercise 8: Predicted vs. Updated Covariance')
plt.xlabel('Time Step (t)')
plt.ylabel('Covariance (Uncertainty)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()