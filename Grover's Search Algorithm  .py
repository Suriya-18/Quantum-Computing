from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

n = 2  # number of qubits (search space: 2^2 = 4)

# Oracle for solution |11⟩
oracle = QuantumCircuit(n)
oracle.cz(0, 1)
oracle = oracle.to_gate()
oracle.name = "Oracle"

# Diffuser
diffuser = QuantumCircuit(n)
diffuser.h(range(n))
diffuser.x(range(n))
diffuser.h(1)
diffuser.cz(0, 1)
diffuser.h(1)
diffuser.x(range(n))
diffuser.h(range(n))
diffuser = diffuser.to_gate()
diffuser.name = "Diffuser"

qc = QuantumCircuit(n, n)
qc.h(range(n))
qc.append(oracle, range(n))
qc.append(diffuser, range(n))
qc.measure(range(n), range(n))

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Grover’s Result:", counts)
plot_histogram(counts)
plt.show()
