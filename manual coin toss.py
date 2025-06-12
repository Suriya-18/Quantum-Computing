from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_vector
import random
import numpy as np

def quantum_coin_toss(verbose=True):
    # Step 1: Picard prepares |0⟩
    qc = QuantumCircuit(1, 1)
    if verbose: print("Picard prepares |0⟩")

    # Step 2: Q applies Hadamard
    qc.h(0)
    if verbose: print("Q applies Hadamard: qubit becomes |+⟩")

    # Step 3: Picard randomly applies I or X
    apply_x = random.choice([True, False])
    if apply_x:
        qc.x(0)
        if verbose: print("Picard applies X (bit flip)")
    else:
        if verbose: print("Picard applies I (does nothing)")

    # Step 4: Q applies Hadamard again
    qc.h(0)
    if verbose: print("Q applies Hadamard again")

    # Step 5: Picard measures the qubit
    qc.measure(0, 0)

    # Execute the circuit
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()

    # Interpret result
    outcome = int(max(counts, key=counts.get))
    if verbose:
        print("Picard measures:", outcome)
        if outcome == 0:
            print("Q wins!")
        else:
            print("Picard wins!")

# Run it
quantum_coin_toss()
