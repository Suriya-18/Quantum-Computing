from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(4)

# Create Bell pairs: (0,1) and (2,3)
qc.h(0)
qc.cx(0, 1)
qc.h(2)
qc.cx(2, 3)

# Bell measurement on 1 and 2
qc.cx(1, 2)
qc.h(1)

sim = Aer.get_backend('statevector_simulator')
state = execute(qc, sim).result().get_statevector()

print("Entangled state (after entanglement swapping):")
print(state)
