import torch
from qiskit.circuit.library import TwoLocal
from qiskit_machine_learning.connectors import TorchConnector
from qiskit_machine_learning.neural_networks import EstimatorQNN

# Build quantum circuit
ansatz = TwoLocal(rotation_blocks='ry', entanglement_blocks='cz')

# Quantum Neural Network
qnn = EstimatorQNN(circuit=ansatz, input_params=[], weight_params=ansatz.parameters)
torch_qnn = TorchConnector(qnn)

# Simple Training Loop (dummy data)
x = torch.rand(5, len(ansatz.parameters))
y = torch.rand(5, 1)

optimizer = torch.optim.Adam(torch_qnn.parameters(), lr=0.1)
loss_fn = torch.nn.MSELoss()

for epoch in range(10):
    optimizer.zero_grad()
    output = torch_qnn(x)
    loss = loss_fn(output, y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1} - Loss: {loss.item()}")
