from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.circuit.library import ZZFeatureMap
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit import Aer

algorithm_globals.random_seed = 123
X, y = make_classification(n_samples=100, n_features=2, n_informative=2,
                           n_redundant=0, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

feature_map = ZZFeatureMap(feature_dimension=2, reps=2)
kernel = QuantumKernel(feature_map=feature_map, quantum_instance=Aer.get_backend('aer_simulator'))
qsvc = QSVC(quantum_kernel=kernel)
qsvc.fit(X_train, y_train)
y_pred = qsvc.predict(X_test)

print("QSVM Accuracy:", accuracy_score(y_test, y_pred))
