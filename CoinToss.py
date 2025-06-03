from qiskit import QuantumCircuit, Aer, execute
import random

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to put the qubit in superposition (equal probability of 0 or 1)
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the circuit using Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit
result = execute(qc, simulator, shots=1).result()

# Get the result (0 or 1)
toss_result = result.get_counts()

# Print the result of the quantum coin toss
print(f"Quantum coin toss result: {random.choice(list(toss_result.keys()))}")
