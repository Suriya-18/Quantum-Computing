from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Quantum teleportation function
def quantum_teleportation():
    # Step 1: Create a quantum circuit with 3 qubits and 3 classical bits
    qc = QuantumCircuit(3, 3)

    # Step 2: Prepare the entangled pair (E1, E2)
    qc.h(1)  # Hadamard gate on qubit 1
    qc.cx(1, 2)  # CNOT gate on qubits 1 and 2 (entangling E1 and E2)
    
    # Step 3: Alice's qubit (A) is in the state |ψ⟩, let's assume it's |0⟩ + |1⟩
    # For simplicity, we start with |0⟩ (Alice's qubit can be in any state)
    qc.h(0)  # Create a superposition state for Alice's qubit (this is her initial state)
    
    # Step 4: Alice performs a Bell-state measurement
    qc.cx(0, 1)  # CNOT gate on Alice's qubit (A) and entangled qubit (E1)
    qc.h(0)  # Hadamard gate on Alice's qubit (A)
    
    # Step 5: Measure Alice's qubit and entangled qubit
    qc.measure([0, 1], [0, 1])  # Measure Alice's and E1's qubits
    
    # Step 6: Bob applies corrections based on Alice's classical bits
    qc.cx(1, 2)  # If Alice sends '1' via classical bits, Bob applies a CNOT
    qc.cz(0, 2)  # If Alice sends '1' via classical bits, Bob applies a Z-gate
    
    # Step 7: Measure Bob's qubit (E2), which is the teleported state
    qc.measure(2, 2)  # Measure Bob's qubit (E2)

    # Simulate the quantum circuit using Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Execute the circuit
    result = execute(qc, simulator, shots=1).result()
    
    # Get the outcome of the measurement
    outcome = result.get_counts(qc)
    
    return outcome

# Run the quantum teleportation simulation
result = quantum_teleportation()
print(f"Quantum Teleportation Result: {result}")

