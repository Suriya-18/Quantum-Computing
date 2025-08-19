from qiskit import QuantumCircuit, Aer, execute

# Define a surface code error correction circuit
def surface_code_circuit():
    qc = QuantumCircuit(5, 4)
    # Create logical qubit using surface code
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.cx(1, 3)
    qc.cx(2, 4)
    # Error correction: measure syndrome bits
    qc.h([1, 2, 3, 4])
    qc.measure([1, 2, 3, 4], [0, 1, 2, 3])  # syndrome extraction
    return qc

surface_code = surface_code_circuit()
backend = Aer.get_backend('qasm_simulator')
result = execute(surface_code, backend, shots=1024).result()
print("Surface code result:", result.get_counts())
