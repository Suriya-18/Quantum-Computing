def bell_test_cheating():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)

    # Cheating attempt: decohere one qubit
    qc.reset(1)  # Wipes entanglement

    qc.measure([0, 1], [0, 1])
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Bell Test with cheating:", result.get_counts())

bell_test_cheating()
