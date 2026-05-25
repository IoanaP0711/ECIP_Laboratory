#modify the length of the weight for state B to 0.5 Plot the evolution of the propagation for 15 steps based on sequence S.
#answer: Does the population survive after the 15th step? Write a report which must contain the plot for these 15 steps and the answer to the question.


import matplotlib.pyplot as plt

# -------------------------------------------------
# Sequence S from the previous exercise
# Replace this example with your own S if needed
# -------------------------------------------------
S = ['A', 'B', 'C', 'A', 'B', 'B', 'C', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'C']

# -------------------------------------------------
# New weights
# A = 1.5, B = 0.5, C = 3.3
# -------------------------------------------------
weights = {
    'A': 1.5,
    'B': 0.5,
    'C': 3.3
}

# -------------------------------------------------
# Initial population
# -------------------------------------------------
population = 0.5

# Store population evolution
pop_values = [population]

# -------------------------------------------------
# Compute propagation for 15 steps based on S
# -------------------------------------------------
for state in S:
    r = weights[state]
    population = population * r
    pop_values.append(population)

# Steps for plotting
steps = list(range(0, len(pop_values)))


plt.figure(figsize=(10, 6))
plt.plot(steps, pop_values, marker='o')
plt.title("Population Propagation for 15 Steps (B weight = 0.5)")
plt.xlabel("Step")
plt.ylabel("Population")
plt.grid(True)
plt.show()


print("Sequence S:", S)
print("Population values:")
for i, val in enumerate(pop_values):
    print(f"Step {i}: {val:.6f}")

print(f"\nPopulation after 15th step: {pop_values[-1]:.6f}")

if pop_values[-1] > 0:
    print("Answer: Yes, the population survives after the 15th step.")
else:
    print("Answer: No, the population does not survive after the 15th step.")