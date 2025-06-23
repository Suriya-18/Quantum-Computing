def bob_wrong_basis():
    from qiskit import QuantumCircuit, Aer, execute
    from qiskit.visualization import plot_histogram

    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Alice sends in |+> basis (expected)

    # Bob measures in Z instead of X
    qc.measure(0, 0)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    counts = result.get_counts()
    print("Bob (wrong basis) measured:", counts)
    plot_histogram(counts).show()

bob_wrong_basis()
