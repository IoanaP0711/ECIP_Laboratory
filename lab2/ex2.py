# use your simulation to point out at what value of r, the population growth becomes chaotic. 
# Show the result in a screenshot. Plot the data.

import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def simulate_logistic(r, x0=0.5, steps=200):
    x = x0
    values = []

    for i in range(steps):
        x = logistic_map(r, x)
        values.append(x)

    return values

# -------------------------------
# Part 1: one example plot
# -------------------------------
r_example = 3.57
values = simulate_logistic(r_example, x0=0.5, steps=100)

plt.figure(figsize=(10, 5))
plt.plot(values, marker='o', markersize=3)
plt.title(f"Logistic Map Population Evolution for r = {r_example}")
plt.xlabel("Time step")
plt.ylabel("Population")
plt.grid(True)
plt.savefig("chaos_example_r357.png")
plt.show()

# -------------------------------
# Part 2: bifurcation diagram
# -------------------------------
r_values = np.linspace(2.5, 4.0, 5000)
x = np.full(len(r_values), 0.5)

# iterate enough times so transient behavior disappears
for _ in range(1000):
    x = logistic_map(r_values, x)

# collect final values for plotting
r_plot = []
x_plot = []

for _ in range(100):
    x = logistic_map(r_values, x)
    r_plot.extend(r_values)
    x_plot.extend(x)

plt.figure(figsize=(12, 7))
plt.plot(r_plot, x_plot, ',k', alpha=0.25)
plt.axvline(3.57, color='red', linestyle='--', label='Approx. chaos starts')
plt.title("Bifurcation Diagram of the Logistic Map")
plt.xlabel("Growth factor r")
plt.ylabel("Population x")
plt.legend()
plt.grid(True)
plt.savefig("bifurcation_diagram.png", dpi=300)
plt.show()

# -------------------------------
# Part 3: text conclusion
# -------------------------------
with open("exercise2_report.txt", "w", encoding="utf-8") as f:
    f.write("EXERCISE 2 REPORT - CHAOS IN THE LOGISTIC MAP\n")
    f.write("=============================================\n\n")
    f.write("Equation used:\n")
    f.write("x(n+1) = r * x(n) * (1 - x(n))\n\n")
    f.write("Conclusion:\n")
    f.write("The population growth becomes chaotic at approximately r = 3.57.\n")
    f.write("A more precise value for the onset of chaos is r = 3.56995.\n\n")
    f.write("Explanation:\n")
    f.write("For small values of r, the population goes to a stable value.\n")
    f.write("When r increases, the system begins to oscillate between 2 values,\n")
    f.write("then 4 values, then 8 values, and so on.\n")
    f.write("After about r = 3.57, the behavior becomes chaotic.\n")
    f.write("This means the population no longer settles into a simple repeating pattern.\n\n")
    f.write("Saved images:\n")
    f.write("- chaos_example_r357.png\n")
    f.write("- bifurcation_diagram.png\n")

print("Done.")
print("Saved files:")
print("- chaos_example_r357.png")
print("- bifurcation_diagram.png")
print("- exercise2_report.txt")