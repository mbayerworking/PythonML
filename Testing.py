# %%

from scipy import sparse

import matplotlib.pyplot as plt
import numpy as np

# %%
eye = np.eye(4)
sparse_matrix = sparse.csr_matrix(eye)

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))

x = np.linspace(-10,10,100)
y = np.sin(x)
# %%
plt.plot(x,y,marker="x")


# %%

eye = np.eye(4)
print("NumPy array:\n{}".format(eye))


# %%

sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))

# %%