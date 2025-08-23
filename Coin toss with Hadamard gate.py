

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def quantum_coin_flip(num_flips=1000):
    """
    Perform a quantum coin flip by applying a Hadamard gate
    to a qubit and measuring multiple times.
    Returns the counts of '0' and '1' outcomes.
    """
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    qc.h(0)           # Apply Hadamard gate for superposition
    qc.measure(0, 0)  # Measure the qubit into the classical bit

    # Use the built-in QASM simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Execute the quantum circuit num_flips times
    result = execute(qc, simulator, shots=num_flips).result()
    counts = result.get_counts(qc)
    return counts

def plot_results(counts):
    plot_histogram(counts)
    plt.title("Quantum Coin Toss Distribution")
    plt.show()

if __name__ == "__main__":
    num_flips = 1000
    counts = quantum_coin_flip(num_flips)
    print(f"Results from {num_flips} quantum coin tosses: {counts}")
    plot_results(counts)
