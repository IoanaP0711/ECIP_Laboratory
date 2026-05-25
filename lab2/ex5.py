# Make a series of experiments in which the population no starts with 
# a. 0.1 b. 0.5 c. 0.9, and r = 4
# make a report in which you note the observations for r.

import matplotlib.pyplot as plt

def logistic_population(r, x0, steps):
    x = x0
    values = [x0]

    for _ in range(steps):
        x = r * x * (1 - x)
        values.append(x)

    return values


# Parameters
r = 4
initial_populations = [0.1, 0.5, 0.9]
steps = 30

# Store all results
results = {}

# Run experiments
for x0 in initial_populations:
    results[x0] = logistic_population(r, x0, steps)

# Plot results
plt.figure(figsize=(12, 7))

for x0, values in results.items():
    plt.plot(range(len(values)), values, marker='o', label=f"x0 = {x0}")

plt.title("Population Evolution for Different Initial Values (r = 4)")
plt.xlabel("Time step")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.savefig("population_experiments_r4.png", dpi=300)
plt.show()

# Create report
with open("report_r4.txt", "w", encoding="utf-8") as f:
    f.write("REPORT: POPULATION EXPERIMENTS FOR r = 4\n")
    f.write("========================================\n\n")
    f.write("Logistic equation used:\n")
    f.write("x(n+1) = r * x(n) * (1 - x(n))\n\n")
    f.write(f"Growth factor: r = {r}\n")
    f.write(f"Initial populations tested: {initial_populations}\n")
    f.write(f"Number of steps: {steps}\n\n")

    for x0, values in results.items():
        f.write(f"Experiment for initial population x0 = {x0}\n")
        f.write("-" * 40 + "\n")
        for i, v in enumerate(values):
            f.write(f"Step {i}: {v}\n")
        f.write("\n")

    f.write("OBSERVATIONS\n")
    f.write("------------\n")
    f.write("For r = 4, the logistic model is in the chaotic region.\n")
    f.write("This means the population does not settle to a single stable value.\n")
    f.write("It also does not follow a simple repeating pattern for most starting values.\n\n")

    f.write("a) For x0 = 0.1:\n")
    f.write("The population changes strongly from one step to another.\n")
    f.write("The values remain between 0 and 1, but the evolution looks irregular.\n\n")

    f.write("b) For x0 = 0.5:\n")
    f.write("The first iteration gives exactly 1.0.\n")
    f.write("After that, the next value becomes 0.0, and then it remains 0.0.\n")
    f.write("So this starting value leads very quickly to extinction.\n\n")

    f.write("c) For x0 = 0.9:\n")
    f.write("The behavior is similar to x0 = 0.1 because the logistic formula is symmetric.\n")
    f.write("The population again shows irregular oscillations.\n\n")

    f.write("GENERAL CONCLUSION\n")
    f.write("------------------\n")
    f.write("For r = 4, the system is extremely sensitive to the initial value.\n")
    f.write("Small changes in the starting population can produce very different results.\n")
    f.write("This is a characteristic of chaotic behavior.\n")
    f.write("The special case x0 = 0.5 leads to collapse to 0.\n")

print("Done.")
print("Saved files:")
print("- population_experiments_r4.png")
print("- report_r4.txt")