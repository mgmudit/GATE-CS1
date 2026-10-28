import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
import sys
import os

# Import line_gen from matgeo
sys.path.insert(0, "CoordGeo")
from line.funcs import *

# Calculate a and b using differentiability
a = 3*1**2 + 2*1
b = 1**3 + 1**2 + 1 - a
print(f"The value of a and b are {a} and {b} respectively")

# Points on the first line: y = ax + b
A = np.array([-2, a*(-2) + b])
B = np.array([1, a*1 + b])

# Generate the straight line using matgeo
x_AB = line_gen(A, B)

# Plot only the portion x < 1
mask = x_AB[0, :] <= 1
plt.plot(x_AB[0, mask], x_AB[1, mask], label="ax + b")

# Plot the second piece: y = x^3 + x^2 + 1
x = np.linspace(1, 3, 500)
y = x**3 + x**2 + 1
plt.plot(x, y, label="x^3 + x^2 + 1")

plt.axvline(1, linestyle="--", alpha=0.5)
plt.grid()
plt.legend()
plt.savefig("plot.pdf")
plt.close()

# Open the generated plot in Termux
subprocess.run(shlex.split("open plot.pdf"))

