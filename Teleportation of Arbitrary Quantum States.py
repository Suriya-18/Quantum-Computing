from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(3, 3)
# Prepare arbitrary quantum state (example: superposition)
qc.h(0)
qc.t(0)  # Apply T gate for more complexity
qc.barrier()

# Create Bell pair between qubit 1 and 2
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Begin teleportation: entangle and measure
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# Measure source qubits
qc.measure([0, 1], [0, 1])

# Classical correction on destination qubit
qc.cx(1, 2)
qc.cz(0, 2)

# Final measurement for verification
qc.measure(2, 2)

# Run simulation
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
counts = job.result().get_counts(qc)
print(counts)
