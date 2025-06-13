from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from math import sqrt
import random

# User-defined parameters
trials = 5
initial_basis = '+'  # Choose from '0', '1', '+', '-'

# Map for basis states
def initialize_qubit(state: str, qc: QuantumCircuit):
    if state == '0':
        pass
    elif state == '1':
        qc.x(0)
    elif state == '+':
        qc.h(0)
    elif state == '-':
        qc.x(0)
        qc.h(0)
        qc.z(0)
    else:
        raise ValueError("Invalid basis state")

# Simulation loop
for i in range(trials):
    print(f"\nTrial {i+1}:")

    qc = QuantumCircuit(1, 1)

    # Q prepares the qubit in chosen state
    initialize_qubit(initial_basis, qc)
    print("  Initially prepared in basis:", initial_basis)

    # Save the state before P
    state_before_p = Statevector.from_instruction(qc)
    print("  Before P's turn:", state_before_p)

    # P's move: randomly apply I or X
    turn = random.choice(['I', 'X'])
    if turn == 'I':
        print("  P passive; applying Identity")
        # No operation
    else:
        print("  P turns; applying X")
        qc.x(0)

    # Q applies Hadamard again
    qc.h(0)

    # Measure final result
    qc.measure(0, 0)

    # Execute
    backend = Aer.get_backend('aer_simulator')
    result = execute(qc, backend, shots=1).result()
    measured = result.get_counts()

    print("  Final measurement:", measured)
