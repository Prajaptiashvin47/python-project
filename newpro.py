import numpy as np  # Import NumPy as np
A = np.array([[3, 1], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

