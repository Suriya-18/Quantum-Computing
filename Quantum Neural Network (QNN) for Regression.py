import numpy as np
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_machine_learning.neural_networks import TwoLayerQNN
from qiskit_machine_learning.connectors import TorchConnector
import torch
from torch import nn
from torch.optim import Adam

# Quantum instance
qi = QuantumInstance(Aer.get_backend("statevector_simulator"))

# Define QNN
num_qubits = 2
qnn = TwoLayerQNN(num_qubits, quantum_instance=qi)

# Convert to PyTorch layer
qnn_layer = TorchConnector(qnn)

# Define model
model = nn.Sequential(qnn_layer, nn.Linear(1, 1))

# Loss and optimizer
loss_fn = nn.MSELoss()
optimizer = Adam(model.parameters(), lr=0.01)

# Dummy regression data
x = torch.rand(20, num_qubits)
y = torch.sin(x[:, 0]) + torch.cos(x[:, 1])
y = y.unsqueeze(1)

# Training loop
for epoch in range(50):
    optimizer.zero_grad()
    output = model(x)
    loss = loss_fn(output, y)
    loss.backward()
    optimizer.step()

print("Training complete, final loss:", loss.item())
