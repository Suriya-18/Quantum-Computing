from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import random

# Define Alice's circuit (prepares the coin)
def alice_prepare():
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Create superposition (fair coin)
    return qc

# Bob's cheating (applies X gate to flip outcome)
def bob_cheat(qc):
    qc.x(0)  # Bit flip: cheating attempt
    return qc

# Alice measures the coin
def alice_measure(qc):
    qc.measure(0, 0)
    return qc

# Full system
def quantum_coin_with_cheating():
    print("Alice: Preparing quantum coin in fair superposition...")
    qc = alice_prepare()

    print("Bob: Intercepting and attempting to cheat...")
    qc = bob_cheat(qc)

    print("Alice: Receiving the coin back and measuring...")
    qc = alice_measure(qc)

    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    
    print("Final Result (cheated):", counts)
    plot_histogram(counts).show()

quantum_coin_with_cheating()
