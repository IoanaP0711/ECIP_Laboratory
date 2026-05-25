#simulate a markov machine containing 3 states: A, B, C.
#Run this machine 15 times and record the sequence of states. store the states as "S"
#Each state carries of weight: A=1.5, B=2, C=3.3
#Use these weights as values for the growth factor r, and calculate the population size of 15 states according to the weights from 5.
# Start the population from 0.5.


import random
import matplotlib.pyplot as plt

# -------------------------------------------------
# Markov machine with the exact numbers from drawing
# -------------------------------------------------
transitions = {
    "A": [("B", 0.4),("C", 0.6)],
    "B": [("A", 0.5), ("B", 0.5)],
    "C": [("A", 0.2), ("B", 0.2), ("C", 0.6)]
}

# State weights
state_weights = {
    "A": 1.5,
    "B": 2.0,
    "C": 3.3
}

# -------------------------------------------------
# Function to choose next state
# -------------------------------------------------
def get_next_state(current_state):
    next_states = [item[0] for item in transitions[current_state]]
    probs = [item[1] for item in transitions[current_state]]
    return random.choices(next_states, weights=probs, k=1)[0]

# -------------------------------------------------
# Logistic population formula
# -------------------------------------------------
def logistic_population(r, x):
    return r * x * (1 - x)

# -------------------------------------------------
# Run the Markov machine 15 times
# -------------------------------------------------
random.seed(42)   # fixed seed for reproducible result

start_state = "A"
S = [start_state]

for _ in range(14):   # total 15 states including the first one
    next_s = get_next_state(S[-1])
    S.append(next_s)

# -------------------------------------------------
# Convert states into r values using state weights
# -------------------------------------------------
r_values = [state_weights[state] for state in S]

# -------------------------------------------------
# Calculate population values
# -------------------------------------------------
x0 = 0.5
population = [x0]

x = x0
for r in r_values:
    x = logistic_population(r, x)
    population.append(x)

# -------------------------------------------------
# Print results
# -------------------------------------------------
print("Sequence of states S:")
print(S)

print("\nWeights used as r values:")
print(r_values)

print("\nPopulation values:")
for i, value in enumerate(population):
    print(f"Step {i}: {value}")

# -------------------------------------------------
# Save results to txt file
# -------------------------------------------------
with open("markov_machine_report.txt", "w", encoding="utf-8") as f:
    f.write("MARKOV MACHINE SIMULATION\n")
    f.write("=========================\n\n")

    f.write("Transitions used exactly as given:\n")
    f.write("A -> B = 0.7\n")
    f.write("A -> C = 0.6\n")
    f.write("B -> A = 0.5\n")
    f.write("B -> B = 0.5\n")
    f.write("C -> A = 0.2\n")
    f.write("C -> B = 0.2\n")
    f.write("C -> C = 0.6\n\n")

    f.write("State weights:\n")
    f.write("A = 1.5\n")
    f.write("B = 2.0\n")
    f.write("C = 3.3\n\n")

    f.write(f"Initial population = {x0}\n\n")

    f.write("Sequence of states S:\n")
    f.write(str(S) + "\n\n")

    f.write("Weights used as growth factor r:\n")
    f.write(str(r_values) + "\n\n")

    f.write("Population values:\n")
    for i, value in enumerate(population):
        f.write(f"Step {i}: {value}\n")

# -------------------------------------------------
# Plot the sequence of states
# -------------------------------------------------
state_to_number = {"A": 1, "B": 2, "C": 3}
numeric_states = [state_to_number[s] for s in S]

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(S) + 1), numeric_states, marker='o')
plt.yticks([1, 2, 3], ["A", "B", "C"])
plt.title("Sequence of States in the Markov Machine")
plt.xlabel("Step")
plt.ylabel("State")
plt.grid(True)
plt.savefig("markov_states.png", dpi=300)
plt.show()

# -------------------------------------------------
# Plot the population values
# -------------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(range(len(population)), population, marker='o')
plt.title("Population Growth Using State Weights as r")
plt.xlabel("Step")
plt.ylabel("Population")
plt.grid(True)
plt.savefig("population_growth_markov.png", dpi=300)
plt.show()

print("\nFiles saved:")
print("- markov_machine_report.txt")
print("- markov_states.png")
print("- population_growth_markov.png")