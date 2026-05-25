# iot noise analysis
# errors: [-1, 2, -2]
# compute squared error
# compare with absolute error
# explain impact on decisions

import numpy as np

# Errors
errors = np.array([-1, 2, -2])

# Compute squared error
squared_error = np.sum(errors ** 2)

# Compute absolute error
absolute_error = np.sum(np.abs(errors))

print("Errors:", errors)
print("Squared error:", squared_error)
print("Absolute error:", absolute_error)

# Explanation:
# Squared error = 1 + 4 + 4 = 9
# Absolute error = 1 + 2 + 2 = 5
#
# Squared error penalizes large errors more strongly because each error is squared.
# Absolute error treats all deviations proportionally.
#
# Impact on decisions:
# - If we use squared error, large mistakes become much more important.
#   This is useful when big errors are dangerous and should be strongly avoided.
# - If we use absolute error, the model is less sensitive to very large individual errors.
#   This is useful when we want a more balanced measure of total error.
# - In IoT systems, squared error is often preferred when large sensor mistakes
#   could lead to wrong control actions or unsafe decisions.