from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_machine_learning.algorithms import QSVM
from qiskit_machine_learning.datasets import ad_hoc_data

# Load dataset
feature_dim = 2
train_features, train_labels, test_features, test_labels, _, _ = ad_hoc_data(
    training_size=20, test_size=10, n=feature_dim, gap=0.3
)

# Backend
backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)

# QSVM model
qsvm = QSVM(train_features, train_labels, test_features, test_labels)
result = qsvm.run(quantum_instance)

print("Training accuracy:", result['training_accuracy'])
print("Test accuracy:", result['test_accuracy'])
