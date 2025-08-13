import pennylane as qml
from pennylane import numpy as np

# 2-qubit device
dev = qml.device("default.qubit", wires=2)

# Example data (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([0, 1, 1, 0])

# Quantum feature map
def feature_map(x):
    qml.RX(np.pi * x[0], wires=0)
    qml.RX(np.pi * x[1], wires=1)
    qml.CNOT(wires=[0, 1])

# Variational quantum circuit
@qml.qnode(dev)
def circuit(params, x):
    feature_map(x)
    qml.RY(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# Cost function
def cost(params):
    predictions = [circuit(params, x) for x in X]
    return np.mean((predictions - Y)**2)

# Train with gradient descent
params = np.random.rand(2, requires_grad=True)
opt = qml.GradientDescentOptimizer(stepsize=0.4)

for _ in range(100):
    params = opt.step(cost, params)

print("Optimized parameters:", params)
print("Predictions:", [circuit(params, x) for x in X])
