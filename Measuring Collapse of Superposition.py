qc = QuantumCircuit(1, 1)
qc.h(0)         # Superposition
qc.measure(0, 0)
qc.barrier()
qc.h(0)
qc.measure(0, 0)

# Only last measurement shows after collapse
result = execute(qc, backend, shots=1000).result()
print("Measurement collapse demo:")
print(result.get_counts())
