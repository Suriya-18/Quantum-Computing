from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def quantum_walk():
    qc = QuantumCircuit(2, 2)
    steps = 3
    for _ in range(steps):
        qc.h(0)                  # Hadamard coin flip
        qc.cx(0, 1)              # Conditional move
    qc.measure([0,1], [0,1])
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    plot_histogram(result.get_counts())

quantum_walk()
