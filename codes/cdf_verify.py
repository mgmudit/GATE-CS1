import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# 1. Theoretical CDF function
def F_theoretical(x):
    x = np.asarray(x, dtype=float)
    return np.piecewise(
        x,
        [x < 1, (x >= 1) & (x <= 4), x > 4],
        [0, lambda x: (x**3 - 1) / 63, 1]
    )

# 2. Simulation using Inverse Transform Method: X = (63U + 1)^(1/3)
N = 100_000
U = np.random.uniform(0, 1, N)
X_simulated = (63 * U + 1) ** (1 / 3)

# 3. Discrete grid points (x = 0.5, 0.75, 1.0, 1.25, 1.5, ..., 4.75)
grid_points = np.arange(0.5, 5.0, 0.25)

# Calculate empirical proportion P(X <= x) at each grid point
simulated_cdf_values = [np.mean(X_simulated <= x) for x in grid_points]

# Smooth theoretical curve for comparison
x_smooth = np.linspace(0, 5, 1000)
y_smooth = F_theoretical(x_smooth)

# Plot canvas setup
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=150)

# Theoretical line
ax.plot(
    x_smooth, y_smooth, 
    label=r'Theoretical CDF: $F(x) = \frac{x^3 - 1}{63}$', 
    color='#1f77b4', linewidth=2
)

# Simulated discrete empirical evaluation points
ax.scatter(
    grid_points, simulated_cdf_values, 
    color='#d62728', zorder=5, 
    label=r'Simulated $P(X \leq x)$ at grid points'
)
ax.plot(
    grid_points, simulated_cdf_values, 
    color='#d62728', linestyle='--', linewidth=1.5, alpha=0.8
)

# Plot formatting
ax.set_title('CDF Verification: Empirical P(X <= x) vs Theoretical F(x)', fontsize=14, pad=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('F(x) = P(X <= x)', fontsize=12)
ax.set_xlim(0, 5)
ax.set_ylim(-0.05, 1.05)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9, fontsize=11)

plt.tight_layout()

# Save image file
output_filename = 'cdf_grid_verification.pdf'
plt.savefig(output_filename)
plt.close()
