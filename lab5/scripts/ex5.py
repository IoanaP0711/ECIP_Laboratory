import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. SETUP & DATA GENERATION
# ==========================================
A, B, C = 1, 1, 1
steps = 30
I = 1

Q = 0.01  # Process noise covariance
R = 0.5   # Measurement noise covariance

np.random.seed(42)

x = np.zeros(steps)
y = np.zeros(steps)
u = np.ones(steps)

w = np.random.normal(0, np.sqrt(Q), steps)
v = np.random.normal(0, np.sqrt(R), steps)

for t in range(steps):
    y[t] = C * x[t] + v[t]
    if t < steps - 1:
        x[t+1] = A * x[t] + B * u[t] + w[t]

# ==========================================
# 2. CASE 1: PREDICTION ONLY
# ==========================================
x_pred_only = np.zeros(steps)

for t in range(1, steps):
    x_pred_only[t] = A * x_pred_only[t-1] + B * u[t]

# ==========================================
# 3. CASE 2: FULL KALMAN FILTER
# ==========================================
x_kf = np.zeros(steps)
P = np.zeros(steps)
x_kf[0] = 0
P[0] = 1.0

for t in range(1, steps):
    # Prediction
    x_pred_temp = A * x_kf[t-1] + B * u[t]
    P_pred = A * P[t-1] * A + Q
    
    # Update
    S = C * P_pred * C + R
    K = (P_pred * C) / S
    
    innovation = y[t] - C * x_pred_temp
    x_kf[t] = x_pred_temp + K * innovation
    P[t] = (I - K * C) * P_pred

# ==========================================
# 4. COMPUTE MEAN SQUARED ERROR (MSE)
# ==========================================
# N is the number of steps (30)
mse_pred_only = np.mean((x - x_pred_only)**2)
mse_kf = np.mean((x - x_kf)**2)

print("=== Mean Squared Error (MSE) Comparison ===")
print(f"1. Prediction Only MSE: {mse_pred_only:.4f}")
print(f"2. Full Kalman Filter MSE: {mse_kf:.4f}")

# ==========================================
# 5. VISUAL COMPARISON
# ==========================================
plt.figure(figsize=(10, 6))
plt.plot(range(steps), x, label='True State $x(t)$', marker='o', color='blue', linewidth=2)
plt.plot(range(steps), x_pred_only, label='Prediction Only $\hat{x}(t|t-1)$', marker='x', linestyle='--', color='orange')
plt.plot(range(steps), x_kf, label='Full Kalman Filter $\hat{x}(t|t)$', marker='s', linestyle='-.', color='green')

plt.title('Comparison: True State vs. Prediction Only vs. Full Kalman Filter')
plt.xlabel('Time Step (t)')
plt.ylabel('State Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()