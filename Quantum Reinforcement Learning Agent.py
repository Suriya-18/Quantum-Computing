import pennylane as qml
from pennylane import numpy as np

n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def q_policy(state, params):
    for i in range(n_qubits):
        qml.RY(state[i], wires=i)
    qml.templates.StronglyEntanglingLayers(params, wires=range(n_qubits))
    return qml.probs(wires=[0, 1])

params = np.random.uniform(low=0, high=np.pi, size=(2, n_qubits, 3))

# Example state
state = np.array([0.5, 0.1])
actions = q_policy(state, params)
print("Action probabilities:", actions)
