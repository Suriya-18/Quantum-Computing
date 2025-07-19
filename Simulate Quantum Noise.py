from qiskit.providers.aer.noise import NoiseModel, depolarizing_error
from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Add depolarizing noise
noise_model = NoiseModel()
error = depolarizing_error(0.1, 1)
noise_model.add_all_qubit_quantum_error(error, ['h'])

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=backend, shots=1024, noise_model=noise_model).result()
counts = result.get_counts()
print("With Noise:", counts)
