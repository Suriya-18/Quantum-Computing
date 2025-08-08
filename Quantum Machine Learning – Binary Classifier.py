import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create synthetic dataset
X, y = make_moons(n_samples=100, noise=0.1, random_state=42)
y = y * 2 - 1  # Convert labels from (0,1) to (-1,1)

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Quantum circuit
n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def circuit(x, weights):
    # Feature encoding
    for i in range(n_qubits):
        qml.RX(x[i], wires=i)
    # Variational layer
    qml.templates.AngleEmbedding(weights, wires=range(n_qubits))
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# Model parameters
weights = np.random.randn(n_qubits, requires_grad=True)

# Loss and accuracy
def square_loss(labels, predictions):
    return np.mean((labels - predictions) ** 2)

def accuracy(labels, predictions):
    preds = np.sign(predictions)
    return np.mean(preds == labels)

# Optimizer
opt = qml.GradientDescentOptimizer(stepsize=0.2)

# Training loop
epochs = 20
for epoch in range(epochs):
    loss = 0
    for x, y_true in zip(X_train, y_train):
        def cost(w): return square_loss(np.array([y_true]), np.array([circuit(x, w)]))
        weights = opt.step(cost, weights)
        loss += cost(weights)
    print(f"Epoch {epoch+1} - Loss: {loss/len(X_train):.4f}")

# Evaluation
predictions = np.array([circuit(x, weights) for x in X_test])
print("Test Accuracy:", accuracy(y_test, predictions))
