from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=10)
result = job.result()
counts = result.get_counts()
print("Random Bits:", counts)
