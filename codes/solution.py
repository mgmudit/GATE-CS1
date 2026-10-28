import numpy as np
import matplotlib.pyplot as plt
import shlex
import subprocess
import sympy as sp
import sys
import os

# Import line_gen from CoordGeo
sys.path.insert(0, "CoordGeo")
from line.funcs import *

print("k = -1 gives infinite solutions, 1 gives no solution, rest other values give unique solution.")
k = int(input("Enter k: "))

x = np.linspace(-1, 1, 1000)

if k == 1:
    y = (1 - x) / k
    y1 = -1 - k*x

elif k == -1:
    y = (1 - x) / k
    y1 = -1 - k*x

else:
    # Coefficient matrix and RHS vector
    a = np.array([[1, k], [k, 1]])
    aS = sp.Matrix(a)
    b = np.array([1, -1])

    y = (1 - x) / k
    y1 = -1 - k*x

    rref = aS.rref()
    p = np.linalg.solve(a, b)

    print("The rref is", rref)
    print("The solution is", p)

# Generate each line using line_gen
A = np.array([-1, (1 - (-1)) / k])
B = np.array([1, (1 - 1) / k])

C = np.array([-1, -1 - k*(-1)])
D = np.array([1, -1 - k*(1)])

x_AB = line_gen(A, B)
x_CD = line_gen(C, D)

# Plot and label both lines
plt.plot(x_AB[0, :], x_AB[1, :], label="x + ky = 1")
plt.plot(x_CD[0, :], x_CD[1, :], label="kx + y = -1")

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"System of equations for k = {k}")
plt.grid(True)
plt.legend()

plt.savefig("intersec.pdf")
plt.close()

subprocess.run(shlex.split("open intersec.pdf"))
