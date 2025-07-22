from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(5,1)
qc.x(0)  # Encode |1⟩

# Encoding
qc.cx(0,1)
qc.cx(0,2)

# Simulate bit flip error on qubit 1
qc.x(1)

# Decode
qc.cx(0,1)
qc.cx(0,2)
qc.ccx(1,2,0)

qc.measure(0,0)

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Corrected Output:", counts)
