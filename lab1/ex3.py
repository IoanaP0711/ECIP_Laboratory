# Estimate the State
# implement a moving average estimator
# compute an estimated signal from noisy observations
# plot the true state, noisy observations, and estimated state 
# a moving average estimator is a method that estimates a signal by averaging recent observations to reduce noise and smooth fluctuations.

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def moving_average(x: np.ndarray, window: int) -> np.ndarray:
    """
    Moving average estimator.
    For each time t, estimate = average of last `window` observations (or fewer at start).
    """
    if window <= 0:
        raise ValueError("window must be >= 1")

    y = np.empty_like(x, dtype=float)
    csum = np.cumsum(x, dtype=float)

    for t in range(len(x)):
        start = max(0, t - window + 1)
        
        s = csum[t] - (csum[start - 1] if start > 0 else 0.0)
        y[t] = s / (t - start + 1)
    return y

def main():
    
    np.random.seed(42)  
    n = 300
    t = np.arange(n)

    
    x_true = 0.01 * t + np.sin(2 * np.pi * t / 50.0)

   
    noise_std = 0.6
    z_obs = x_true + np.random.normal(0, noise_std, size=n)

    
    window = 15
    x_hat = moving_average(z_obs, window)

    
    plt.figure(figsize=(12, 5))
    plt.plot(t, x_true, label="True state (x_true)", linewidth=2)
    plt.scatter(t, z_obs, label="Noisy observations (z_obs)", s=12, alpha=0.6)
    plt.plot(t, x_hat, label=f"Estimated state (moving avg, window={window})", linewidth=2)

    plt.title("State Estimation with Moving Average")
    plt.xlabel("Time (t)")
    plt.ylabel("Signal value")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()