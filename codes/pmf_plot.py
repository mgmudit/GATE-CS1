import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Sample size
simlen = 10000

# Possible number of sixes
n = np.arange(0, 4)

# Generate three independent die rolls per experiment
y = np.random.randint(1, 7, size=(3, simlen))

# Count the number of sixes in each experiment
X = np.sum(y == 6, axis=0)

# Find the frequency of each possible outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated PMF
psim = np.zeros(4)
psim[unique] = counts / simlen

# Theoretical PMF
panal = np.array([
    comb(3, k) * (1/6)**k * (5/6)**(3-k)
    for k in n
])

# Print the PMFs
print("X | Simulated PMF | Theoretical PMF")
print("-----------------------------------")

for k in n:
    print(f"{k} | {psim[k]:.6f}       | {panal[k]:.6f}")

print("\nProbability of exactly one six:")
print("Simulated:", psim[1])
print("Theoretical:", panal[1])

# Plotting
plt.stem(n, psim, markerfmt='o', label='Simulation')
plt.stem(n, panal, markerfmt='x', label='Analysis')

plt.xlabel('Number of sixes (k)')
plt.ylabel('$p_X(k)$')
plt.title('PMF: Three Die Rolls')
plt.legend()
plt.grid()

plt.savefig('../figs/pmf_plot.pdf')
plt.show()
