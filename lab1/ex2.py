# Generate Noisy Observations
# generate noisy observations: y(t) = x(t)+noise
# use gaussian noise with mean 0 and standard deviation 2
# plot true state and observations on the same graph

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


steps = 50
x0 = 0

x = [x0]
for _ in range(steps):
    x.append(x[-1] + 1)

t = np.arange(steps + 1)


np.random.seed(42)  
noise = np.random.normal(loc=0.0, scale=2.0, size=steps + 1)
y = np.array(x) + noise


plt.figure(figsize=(9, 4))
plt.plot(t, x, marker="o", linewidth=2, label="True state x(t)")
plt.scatter(t, y, s=25, label="Observations y(t)")
plt.title("True State vs Noisy Observations (μ=0, σ=2)")
plt.xlabel("Time step t")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.tight_layout()


plt.savefig("ex2_true_vs_observations.png", dpi=200)
plt.show()

print("Saved plot to: ex2_true_vs_observations.png")