from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
import numpy as np

qc = QuantumCircuit(3, 2)

# Prepare eigenstate of unitary (|1⟩ for Z gate)
qc.x(2)

# Apply Hadamards to counting qubits
qc.h([0,1])

# Controlled-U operations (U = Z)
qc.cz(1,2)
qc.cz(0,2)
qc.cz(0,2)  # U^2

# Inverse QFT
inv_qft = QFT(2, inverse=True).to_gate()
qc.append(inv_qft, [0,1])
qc.measure([0,1], [0,1])

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Phase Estimation Result:", counts)
