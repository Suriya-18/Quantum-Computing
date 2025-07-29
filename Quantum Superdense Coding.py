from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2, 2)

# Shared entangled pair
qc.h(0)
qc.cx(0, 1)

# Alice encodes message "10"
qc.z(0)  # flips phase
qc.barrier()

# Bob decodes
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()

print("Superdense Coding output:")
print(counts)
