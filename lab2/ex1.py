# make a simulation by using the logistic regression expression = people growth. Use a growth factor r=0.9.
# make a report (.txt file) that describes the fate of the population for r=9.

import matplotlib.pyplot as plt

def logistic_simulation(r, x0, steps):
    values = [x0]
    x = x0

    for _ in range(steps):
        x = r * x * (1 - x)
        values.append(x)

    return values


def make_report(filename, values, r):
    with open(filename, "w") as f:
        f.write("LOGISTIC POPULATION GROWTH REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Growth factor r = {r}\n")
        f.write(f"Initial population x0 = {values[0]}\n")
        f.write(f"Number of steps = {len(values) - 1}\n\n")

        f.write("Population values:\n")
        for i, v in enumerate(values):
            f.write(f"Step {i}: {v}\n")

        f.write("\nInterpretation:\n")

        if r < 1:
            f.write(
                "For r < 1, the population decreases over time and tends toward 0.\n"
                "This means the population eventually dies out.\n"
            )
        elif 1 <= r <= 3:
            f.write(
                "For 1 <= r <= 3, the population tends to a stable value.\n"
            )
        elif 3 < r <= 4:
            f.write(
                "For 3 < r <= 4, the population may oscillate or behave chaotically.\n"
            )
        else:
            f.write(
                "For r > 4, the logistic equation no longer gives a realistic population model.\n"
                "The values usually leave the interval [0, 1], so the result becomes unstable\n"
                "and has no physical meaning for normalized population growth.\n"
            )


# -------------------------------
# Part 1: simulation for r = 0.9
# -------------------------------
r_sim = 0.9
x0 = 0.2
steps = 50

values_r09 = logistic_simulation(r_sim, x0, steps)

plt.figure(figsize=(10, 5))
plt.plot(range(len(values_r09)), values_r09, marker='o')
plt.title("Logistic Population Growth Simulation (r = 0.9)")
plt.xlabel("Time step")
plt.ylabel("Population")
plt.grid(True)
plt.show()


# --------------------------------
# Part 2: report for r = 9
# --------------------------------
r_report = 9
values_r9 = logistic_simulation(r_report, x0, steps)
make_report("population_report_r9.txt", values_r9, r_report)

print("Simulation done.")
print("Report saved as population_report_r9.txt")