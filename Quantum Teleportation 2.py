from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, Aer, execute
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import random

# Step 1: Initialize qubits
q = QuantumRegister(3)  # q0 = z, q1 = x, q2 = y
c = ClassicalRegister(2)  # c0 = result z, c1 = result x
qc = QuantumCircuit(q, c)

# Step 2: Choose initial qubit state for teleportation (z)
state_choice = random.choice(['0', '1', '+', '-'])
if state_choice == '0':
    pass  # |0>
elif state_choice == '1':
    qc.x(q[0])  # |1>
elif state_choice == '+':
    qc.h(q[0])  # |+>
elif state_choice == '-':
    qc.x(q[0])
    qc.h(q[0])
    qc.z(q[0])  # |−>

print(f"Alice's initial qubit z is |{state_choice}⟩")

# Step 3: Entangle x and y
qc.h(q[1])
qc.cx(q[1], q[2])

# Step 4: Bell measurement between z and x
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

# Step 5: Conditional operations on y (teleported qubit)
qc.x(q[2]).c_if(c, 1)  # if c = 01 or 11
qc.z(q[2]).c_if(c, 2)  # if c = 10 or 11

# Execute
sim = Aer.get_backend('aer_simulator')
qc = qc.reverse_bits()
result = execute(qc, sim, shots=1, memory=True).result()
output = result.get_memory()[0]

print(f"Classical bits sent to Bob: {output}")
print("Qubit has been teleported to Bob (q2)")
qc.draw('mpl')
