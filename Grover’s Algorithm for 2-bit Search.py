from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Oracle that flips |11⟩
oracle = QuantumCircuit(2)
oracle.cz(0, 1)

# Grover's diffusion operator
def diffuser(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    return qc

qc = QuantumCircuit(2, 2)
qc.h([0, 1])
qc = qc.compose(oracle)
qc = qc.compose(diffuser(2))
qc.measure([0, 1], [0, 1])

sim = Aer.get_backend('qasm_simulator')
result = execute(qc, sim, shots=1024).result()
counts = result.get_counts()
print("Result:", counts)
