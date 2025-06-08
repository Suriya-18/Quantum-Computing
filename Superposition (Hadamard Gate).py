from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply the Hadamard gate (H) to create superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Use the Aer simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit
result = execute(qc, simulator, shots=1024).result()

# Get and print the result
counts = result.get_counts()
print(counts)
