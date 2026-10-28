import numpy as np
import matplotlib.pyplot as plt

# Normalize the probability density
C = 1/21
print("P(2 <= x <= 3) =", C*(3**3 - 2**3)/3)

# Generate x-values for the full domain [0, 5]
x = np.linspace(0, 5, 500)
# P(x) is 0 outside [1, 4]
y = np.where((x >= 1) & (x <= 4), C*x**2, 0)

# Plot the density curve
plt.plot(x, y, label="P(x) = x²/21")

# Shade the region from x = 2 to x = 3
xs = np.linspace(2, 3, 200)
plt.fill_between(xs, C*xs**2, alpha=0.3, label="Probability")

# Set x-axis limits from 0 to 5
plt.xlim(0, 5)
plt.ylim(-0.05, 0.85)

plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Probability Density Function")
plt.grid()
plt.legend()
plt.savefig("plt.pdf")
plt.close()
