import numpy as np
import matplotlib.pyplot as plt
import subprocess
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

# Label each point with its probability
for i in range(len(k)):
    plt.annotate(f"{prob[i]:.6f}", (k[i], prob[i]),
                 textcoords="offset points", xytext=(0, 8),
                 ha="center", fontsize=9)

plt.xlabel("Number of flipped bits (k)")
plt.ylabel("Probability P(Y = k)")
plt.title("Error Distribution for a 5-Bit Message")
plt.xticks(k)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig("errordistri.pdf", bbox_inches="tight")
plt.close()
subprocess.run(["open", "errordistri.pdf"])

