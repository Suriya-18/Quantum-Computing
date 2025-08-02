from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def bit_flip_code():
    qc = QuantumCircuit(5, 1)

    # Encode logical qubit (|+⟩ state)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Introduce bit-flip error on qubit 1
    qc.x(1)

    # Syndrome measurement
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(1, 4)
    qc.cx(2, 4)

    # Correct the error based on classical measurement
    qc.measure(0, 0)  # Optional: measure logical qubit
    qc.draw('mpl')

    result = execute(qc, Aer.get_backend("qasm_simulator"), shots=1024).result()
    counts = result.get_counts()
    plot_histogram(counts)

bit_flip_code()
