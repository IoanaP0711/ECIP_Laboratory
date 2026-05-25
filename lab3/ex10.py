# conditional probability
# simulate P(A|B) from data
# interpret conditional probability

import numpy as np

# Number of samples
n = 10000

# Simulate two events A and B (Bernoulli variables)
# Example: A happens with probability 0.5, B with probability 0.4
A = np.random.rand(n) < 0.5
B = np.random.rand(n) < 0.4

# Compute P(A | B)
# Count how many times B happens
B_count = np.sum(B)

# Count how many times both A and B happen
A_and_B_count = np.sum(A & B)

# Conditional probability
P_A_given_B = A_and_B_count / B_count

# Also compute P(A ∩ B) and P(B)
P_A_and_B = A_and_B_count / n
P_B = B_count / n

print("P(A ∩ B):", P_A_and_B)
print("P(B):", P_B)
print("P(A | B):", P_A_given_B)

# Verify formula: P(A|B) = P(A ∩ B) / P(B)
print("Check:", P_A_and_B / P_B)