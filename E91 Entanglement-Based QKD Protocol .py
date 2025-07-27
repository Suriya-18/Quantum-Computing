from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.barrier()
qc.h(0)
qc.h(1)
qc.measure([0, 1], [0, 1])

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
counts = job.result().get_counts()

print("E91 Output (should show strong correlations):")
print(counts)
