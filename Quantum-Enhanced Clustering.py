from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit import Aer
from sklearn.cluster import KMeans
import numpy as np

# Classical dataset
X = np.array([[0,0], [1,1], [1,0], [0,1]])

# Define quantum kernel
feature_map = ZZFeatureMap(2, reps=2)
quantum_kernel = QuantumKernel(feature_map, quantum_instance=Aer.get_backend('statevector_simulator'))

# Compute kernel matrix
kernel_matrix = quantum_kernel.evaluate(X)

# Apply classical clustering with quantum kernel
kmeans = KMeans(n_clusters=2, random_state=0).fit(kernel_matrix)

print("Cluster assignments:", kmeans.labels_)
