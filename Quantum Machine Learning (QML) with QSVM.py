from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.circuit.library import ZZFeatureMap
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create dummy dataset
X, y = make_classification(n_samples=20, n_features=2, n_informative=2, n_redundant=0)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Define quantum kernel and QSVM
feature_map = ZZFeatureMap(feature_dimension=2, reps=2)
quantum_kernel = QuantumKernel(feature_map=feature_map, quantum_instance=Aer.get_backend('aer_simulator'))
qsvc = QSVC(quantum_kernel=quantum_kernel)

# Train and evaluate
qsvc.fit(X_train, y_train)
accuracy = qsvc.score(X_test, y_test)
print("QSVM Test Accuracy:", accuracy)
