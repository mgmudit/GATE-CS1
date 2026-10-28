import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Compute values
n_max = 15
n_vals = np.arange(0, n_max + 1)

# Numerical iteration
T_num = np.zeros(n_max + 1, dtype=np.int64)
T_num[0] = 1
for n in range(1, n_max + 1):
    T_num[n] = 2 * T_num[n - 1] + n * (2**n)

# Theoretical formula
T_theory = (2**n_vals) * (1 + n_vals / 2 + (n_vals**2) / 2)

# 2. Generate Plot
plt.figure(figsize=(9, 5))
plt.plot(
    n_vals,
    T_num,
    "ro-",
    label="Numerical (Recurrence Iteration)",
    markersize=8,
    linewidth=2,
)
plt.plot(
    n_vals,
    T_theory,
    "b--",
    label=r"Theoretical Formula: $T(n) = 2^n\left(1 + \frac{n}{2} + \frac{n^2}{2}\right)$",
    linewidth=2,
)

plt.title(
    r"Comparison of Numerical vs Theoretical Solution for $T(n) = 2T(n-1) + n 2^n$",
    fontsize=12,
    pad=12,
)
plt.xlabel("n", fontsize=11)
plt.ylabel("T(n)", fontsize=11)
plt.yscale("log")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()

# 3. Save plot to file
image_name = "graph.pdf"
plt.savefig(image_name, dpi=300)
plt.close()  # Close plot memory without calling plt.show()

# 4. Automatically open the image on Android/Termux
if os.system(f"termux-open {image_name}") != 0:
    # Fallback for Linux/Mac/Windows if not running in Termux
    os.system(f"xdg-open {image_name} || open {image_name}")
