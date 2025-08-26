import pennylane as qml
from pennylane import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

# Define a quantum layer
@qml.qnode(dev, interface="torch")
def quantum_layer(inputs, weights):
    for i in range(n_qubits):
        qml.RX(inputs[i], wires=i)
        qml.RY(inputs[i], wires=i)
    qml.templates.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

weight_shapes = {"weights": (3, n_qubits, 3)}
qlayer = qml.qnn.TorchLayer(quantum_layer, weight_shapes)

# Classical model + quantum layer
model = nn.Sequential(
    nn.Linear(n_qubits, n_qubits),
    nn.ReLU(),
    qlayer,
    nn.Linear(n_qubits, 2),
    nn.LogSoftmax(dim=1)
)

# Example training
x = torch.rand((5, n_qubits)) * np.pi
y = torch.randint(0, 2, (5,))

criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(5):
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
