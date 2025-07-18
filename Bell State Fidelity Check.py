from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import state_fidelity, Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Simulate state
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
state = result.get_statevector()

# Expected Bell state: (|00⟩ + |11⟩) / sqrt(2)
ideal = (Statevector.from_label('00') + Statevector.from_label('11')) / 2**0.5

fidelity = state_fidelity(state, ideal)
print("Fidelity with Bell state:", fidelity)
