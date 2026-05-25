import numpy as np
import matplotlib.pyplot as plt

# --- 1. System Parameters ---
steps = 30
np.random.seed(42)

x = np.zeros(steps)
u = np.sin(np.linspace(0, 5, steps)) # Oscillating input
w = np.random.normal(0, 0.1, steps)  # Small process noise

x[0] = 0.5 # Small initial state

# --- 2. Simulate Nonlinear System ---
for t in range(steps - 1):
    # Nonlinear dynamics: x(t+1) = x(t) + 0.1*x(t)^2 + u(t) + w(t)
    x[t+1] = x[t] + 0.1 * (x[t]**2) + u[t] + w[t]

# --- 3. Plotting ---
plt.figure(figsize=(10, 5))
plt.plot(range(steps), x, label='Nonlinear State $x(t)$', color='purple', marker='o')
plt.plot(range(steps), u, label='Input $u(t)$', color='gray', linestyle='--')
plt.title('Exercise 11: Nonlinear System Simulation')
plt.xlabel('Time Step (t)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()