from qiskit import QuantumCircuit, Aer, transpile, assemble
import numpy as np
from qiskit.visualization import plot_histogram

# Step 1: Define the BB84 protocol functions

# Alice's bit preparation and sending
def alice_send(bits, bases):
    n = len(bits)
    qc = QuantumCircuit(n, n)

    # Alice's encoding
    for i in range(n):
        if bits[i] == 1:
            qc.x(i)  # Apply X gate (bit-flip) if bit is 1

        # Select random basis for encoding
        if bases[i] == 'X':
            qc.h(i)  # Hadamard gate for X basis
        # No need for basis change for Z basis

    # Alice sends the qubits to Bob
    qc.measure(range(n), range(n))
    return qc

# Bob's measurement
def bob_receive(bases, n):
    qc = QuantumCircuit(n, n)

    # Bob's measurement
    for i in range(n):
        if bases[i] == 'X':
            qc.h(i)  # Apply Hadamard gate to switch to X basis

    # Measure the qubits
    qc.measure(range(n), range(n))
    return qc

# Step 2: Key sifting - Compare bases and keep bits where bases match
def sift_keys(alice_bits, alice_bases, bob_bases, counts_bob):
    key = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_bits[i])
    return key

# Step 3: Simulate the QKD process

# Number of qubits (bits)
n = 4

# Generate random bits and bases for Alice
alice_bits = np.random.randint(2, size=n)  # Alice's random bits (0 or 1)
alice_bases = np.random.choice(['Z', 'X'], size=n)  # Alice's random bases (Z or X)

# Generate random bases for Bob
bob_bases = np.random.choice(['Z', 'X'], size=n)  # Bob's random bases (Z or X)

# Alice prepares the qubits and sends them to Bob
qc = alice_send(alice_bits, alice_bases)

# Simulate the quantum circuit using Aer backend (classical simulation)
simulator = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, simulator)
qobj = assemble(tqc)
result = simulator.run(qobj).result()

# Get the measurement results from Bob
counts = result.get_counts()

# Bob performs his measurement based on his randomly chosen bases
bob_qc = bob_receive(bob_bases, n)
tqc_bob = transpile(bob_qc, simulator)
qobj_bob = assemble(tqc_bob)
result_bob = simulator.run(qobj_bob).result()
counts_bob = result_bob.get_counts()

# Step 4: Perform key sifting
final_key = sift_keys(alice_bits, alice_bases, bob_bases, counts_bob)

# Output the results
print(f"Alice's bits: {alice_bits}")
print(f"Alice's bases: {alice_bases}")
print(f"Bob's bases: {bob_bases}")
print(f"Bob's measured bits (Counts): {counts_bob}")
print(f"Final shared key: {final_key}")
