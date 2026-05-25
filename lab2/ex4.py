# Consider the above vector as values for r factor, measured here, across 17 years. 
# Answer "What will be the population growth in the 17th year?"

import matplotlib.pyplot as plt

# Values of r for 17 years
r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

# Initial population
x0 = 0.5

# Current population
x = x0

# Store population values for plotting
population_values = [x0]

print("Population growth over 17 years:\n")

# Calculate population year by year
for year, r in enumerate(r_values, start=1):
    x = r * x * (1 - x)
    population_values.append(x)
    print(f"Year {year}: r = {r}, population = {x}")

print("\nPopulation in the 17th year:")
print(x)

# Save result to txt file
with open("population_17th_year_report.txt", "w", encoding="utf-8") as f:
    f.write("POPULATION GROWTH OVER 17 YEARS\n")
    f.write("================================\n\n")
    f.write(f"Initial population x0 = {x0}\n")
    f.write(f"r values = {r_values}\n\n")

    for year, value in enumerate(population_values[1:], start=1):
        f.write(f"Year {year}: population = {value}\n")

    f.write("\nFinal answer:\n")
    f.write(f"The population in the 17th year is: {x}\n")

# Plot the population growth
plt.figure(figsize=(10, 6))
plt.plot(range(0, len(population_values)), population_values, marker='o')
plt.title("Population Growth Over 17 Years")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)

# Save plot
plt.savefig("population_17th_year_plot.png", dpi=300)

# Show plot
plt.show()

print("\nFiles saved:")
print("- population_17th_year_report.txt")
print("- population_17th_year_plot.png")