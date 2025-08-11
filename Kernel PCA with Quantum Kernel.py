# pip: qiskit qiskit-machine-learning scikit-learn
from qiskit.circuit.library import ZZFeatureMap
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_machine_learning.kernels import QuantumKernel
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=80, centers=3, n_features=2, random_state=1)
feature_map = ZZFeatureMap(feature_dimension=2, reps=1)
qi = QuantumInstance(Aer.get_backend("qasm_simulator"), shots=512)
qk = QuantumKernel(feature_map=feature_map, quantum_instance=qi)
K = qk.evaluate(x_vec=X)   # kernel matrix
pca = PCA(n_components=2)
Z = pca.fit_transform(K)   # kernel PCA on quantum kernel
print("Transformed shape:", Z.shape)
