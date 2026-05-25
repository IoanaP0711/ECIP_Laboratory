import matplotlib.pyplot as plt

def logistic_population(r, x0, steps):
    x = x0
    values = [x0]

    for _ in range(steps):
        x = r * x * (1 - x)
        values.append(x)

    return values


r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
x0 = 0.5
steps = 30

final_populations = []

# plot population evolution
plt.figure(figsize=(12, 7))
for r in r_values:
    population = logistic_population(r, x0, steps)
    final_populations.append(population[-1])
    plt.plot(population, label=f"r={r}")

plt.title("Population size evolution for different values of r")
plt.xlabel("Time step")
plt.ylabel("Population size")
plt.legend()
plt.grid(True)
plt.show()

# print final values
print("\nFinal population values:")
for r, final_value in zip(r_values, final_populations):
    print(f"r = {r}, final population = {final_value}")

# plot final populations
plt.figure(figsize=(10, 6))
plt.plot(r_values, final_populations, marker='o')
plt.title("Final population size for each r")
plt.xlabel("r")
plt.ylabel("Final population size")
plt.grid(True)
plt.show()