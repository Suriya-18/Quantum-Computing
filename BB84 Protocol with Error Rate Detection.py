from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import random

def generate_bb84_key(length=100):
    alice_bits = [random.randint(0, 1) for _ in range(length)]
    alice_bases = [random.choice(['Z', 'X']) for _ in range(length)]
    bob_bases = [random.choice(['Z', 'X']) for _ in range(length)]
    bob_results = []

    for i in range(length):
        qc = QuantumCircuit(1, 1)
        if alice_bits[i] == 1:
            qc.x(0)
        if alice_bases[i] == 'X':
            qc.h(0)
        qc.barrier()
        if bob_bases[i] == 'X':
            qc.h(0)
        qc.measure(0, 0)

        backend = Aer.get_backend('qasm_simulator')
        result = execute(qc, backend, shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        bob_results.append(measured_bit)

    # Key Sifting
    sifted_key = [bob_results[i] for i in range(length) if bob_bases[i] == alice_bases[i]]
    error_check_sample = sifted_key[:10]  # Publicly shared to detect eavesdropping

    print("Sifted Key:", sifted_key)
    print("Sample for Error Rate Checking (shared):", error_check_sample)

generate_bb84_key()
