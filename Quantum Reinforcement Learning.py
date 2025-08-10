# pip: pennylane torch
import pennylane as qml
from pennylane import numpy as np
import torch

n_actions = 2
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev, interface="torch")
def policy_circuit(weights, obs):
    qml.RY(obs[0], wires=0)
    qml.RY(obs[1], wires=1)
    qml.templates.StronglyEntanglingLayers(weights, wires=[0,1])
    return qml.expval(qml.PauliZ(0)), qml.expval(qml.PauliZ(1))

# Convert to PyTorch module
class QuantumPolicy(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = torch.nn.Parameter(0.01 * torch.randn(1,2,3))
    def forward(self, obs):
        z = policy_circuit(self.weights, torch.tensor(obs, dtype=torch.float32))
        probs = torch.softmax(torch.stack(z), dim=0)
        return probs

# Use REINFORCE update (sketch)
policy = QuantumPolicy()
opt = torch.optim.Adam(policy.parameters(), lr=0.01)
# run episodes, compute returns, update policy via log-prob * return
