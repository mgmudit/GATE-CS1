import numpy as np
import matplotlib.pyplot as plt
from math import comb

n = 5
p = 0.01
k = np.arange(n + 1)

# Calculate binomial probabilities
prob = np.array([
    comb(n, i) * p**i * (1-p)**(n-i)
    for i in k
])

print("P(error-free) =", prob[0])

# Step plot with labels
plt.step(k, prob, where="mid", label="P(Y = k)")
plt.scatter(k, prob)

# Annotate each point individually without using loops
plt.annotate(f"{prob[0]:.6f}", (k[0], prob[0]), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)
plt.annotate(f"{prob[1]:.6f}", (k[1], prob[1]), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)
plt.annotate(f"{prob[2]:.6f}", (k[2], prob[2]), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)
plt.annotate(f"{prob[3]:.6f}", (k[3], prob[3]), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)
plt.annotate(f"{prob[4]:.6f}", (k[4], prob[4]), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)
plt.annotate(f"{prob[5]:.6f}", (k[5], prob[5]), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)

plt.xlabel("Number of flipped bits (k)")
plt.ylabel("Probability P(Y = k)")
plt.title("Error Distribution for a 5-Bit Message")
plt.xticks(k)
plt.ylim(-0.05, 1.15)
plt.xlim(-0.5, 5.5)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig("../figs/errordistri.pdf", bbox_inches="tight")
plt.close()
