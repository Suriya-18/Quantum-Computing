from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1).result()
print(result.get_counts())
