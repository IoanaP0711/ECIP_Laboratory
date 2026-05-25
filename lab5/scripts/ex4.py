import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. SETUP & DATA GENERATION
# ==========================================
A, B, C = 1, 1, 1
steps = 30
I = 1 # Identity matrix (scalar 1 in a 1D system)

# Filter parameters from the slide
Q = 0.01  # Process noise covariance
R = 0.5   # Measurement noise covariance
P_init = 1.0  # P(0|0)
x_hat_init = 0.0 # \hat{x}(0|0) from previous exercise

np.random.seed(42)

x = np.zeros(steps)
y = np.zeros(steps)
u = np.ones(steps)

# Generate true noise using Q and R as variances
# Standard deviation is the square root of variance
w = np.random.normal(0, np.sqrt(Q), steps)
v = np.random.normal(0, np.sqrt(R), steps)

# Generate true state and measurements
for t in range(steps):
    y[t] = C * x[t] + v[t]
    if t < steps - 1:
        x[t+1] = A * x[t] + B * u[t] + w[t]

# ==========================================
# 2. FULL KALMAN FILTER IMPLEMENTATION
# ==========================================
# Pre-allocate arrays for estimates
x_hat = np.zeros(steps)      # \hat{x}(t|t) - Updated state estimate
x_pred = np.zeros(steps)     # \hat{x}(t|t-1) - Predicted state estimate
P = np.zeros(steps)          # P(t|t) - Updated covariance
P_pred = np.zeros(steps)     # P(t|t-1) - Predicted covariance
K = np.zeros(steps)          # K(t) - Kalman Gain

# Apply initial conditions
x_hat[0] = x_hat_init
P[0] = P_init

# Run the filter from t=1 to steps-1
for t in range(1, steps):
    # --- PREDICTION STEP ---
    # 1. State Prediction: \hat{x}(t|t-1) = A\hat{x}(t-1|t-1) + Bu(t)
    x_pred[t] = A * x_hat[t-1] + B * u[t]
    
    # 2. Covariance Prediction: P(t|t-1) = A*P(t-1|t-1)*A^T + Q
    P_pred[t] = A * P[t-1] * A + Q 

    # --- UPDATE STEP ---
    # 3. Kalman Gain: K(t) = P(t|t-1)*C^T * (C*P(t|t-1)*C^T + R)^-1
    # In 1D, transpose is itself, and inverse is division
    S = C * P_pred[t] * C + R
    K[t] = (P_pred[t] * C) / S
    
    # 4. State Update: \hat{x}(t|t) = \hat{x}(t|t-1) + K(t)(y(t) - C\hat{x}(t|t-1))
    innovation = y[t] - C * x_pred[t]
    x_hat[t] = x_pred[t] + K[t] * innovation
    
    # 5. Covariance Update: P(t|t) = (I - K(t)C) * P(t|t-1)
    P[t] = (I - K[t] * C) * P_pred[t]

# ==========================================
# 3. PLOTTING
# ==========================================

# Plot 1: True State, Noisy Measurement, and Kalman Estimate
plt.figure(figsize=(10, 5))
plt.plot(range(steps), x, label='True State $x(t)$', marker='o', linestyle='-', color='blue')
plt.plot(range(steps), y, label='Noisy Measurement $y(t)$', marker='x', linestyle='', color='red', alpha=0.6)
plt.plot(range(steps), x_hat, label='Kalman Estimate $\hat{x}(t|t)$', marker='s', linestyle='--', color='green')
plt.title('Kalman Filter: State Estimation')
plt.xlabel('Time Step (t)')
plt.ylabel('State Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Kalman Gain and Covariance over time
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Kalman Gain Subplot
# Note: K[0] is 0 because we started filtering at t=1, so we plot from t=1 onwards
ax1.plot(range(1, steps), K[1:], label='Kalman Gain $K(t)$', color='darkorange', marker='^', linestyle='-')
ax1.set_title('Kalman Gain $K(t)$ over Time')
ax1.set_ylabel('Gain Value')
ax1.legend()
ax1.grid(True)

# Covariance Subplot
ax2.plot(range(steps), P, label='Error Covariance $P(t|t)$', color='purple', marker='v', linestyle='-')
ax2.set_title('Error Covariance $P(t|t)$ over Time')
ax2.set_xlabel('Time Step (t)')
ax2.set_ylabel('Covariance Value')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()