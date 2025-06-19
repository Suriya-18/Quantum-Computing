def quantum_bit_commitment(commit_bit=0):
    qc = QuantumCircuit(1, 1)

    if commit_bit == 0:
        qc.h(0)
    else:
        qc.x(0)
        qc.h(0)
    qc.barrier()

    # Later reveal
    if commit_bit == 0:
        qc.h(0)
    else:
        qc.h(0)
        qc.x(0)

    qc.measure(0, 0)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    counts = result.get_counts()
    print(f"Bob’s committed bit: {commit_bit}, Reveal Result:", counts)
    plot_histogram(counts).show()

quantum_bit_commitment(commit_bit=1)
