import matplotlib.pyplot as plt
import numpy as np

# Define the cumulative distribution function F(x)
def cdf(x):
    return np.piecewise(x, 
                        [x < 1, (x >= 1) & (x <= 4), x > 4], 
                        [0.0, lambda x: (x**3 - 1) / 63, 1.0])

# Generate x values across and beyond the domain
x = np.linspace(0, 5, 500)
y = cdf(x)

# Create high-resolution plot with thin lines and grid
plt.figure(figsize=(8, 5), dpi=300)
plt.plot(x, y, color='blue', linewidth=0.5, label='F(x) = (x^3 - 1) / 63')

plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-0.05, 1.05)
plt.legend()

# Save the figure locally
filename = 'cdf_plot.pdf'
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
