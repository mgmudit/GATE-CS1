import numpy as np

# Define matrix A
A = np.array([[1, 1],
              [1, -1]])

# Calculate A^13
A13 = np.linalg.matrix_power(A, 13)

# Calculate eigenvalues of A^13
eigenvalues = np.linalg.eigvals(A13)

print("A^13 =\n", A13)
print("Eigenvalues of A^13 =", eigenvalues)

