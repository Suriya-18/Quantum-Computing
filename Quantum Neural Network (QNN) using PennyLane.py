import pennylane as qml
from pennylane import numpy as np

n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def qnn(weights, x):
    for i in range(n_qubits):
        qml.RX(x[i], wires=i)
        qml.RY(weights[i], wires=i)
    qml.CNOT(wires=[0, 1])
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Example input and weights
x = np.array([0.5, 1.0])
weights = np.array([0.1, 0.2])

print("QNN Output:", qnn(weights, x))
