def quantum_lottery_cheating():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Fair coin

    # Host cheats
    qc.x(0)

    qc.measure(0, 0)
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Quantum Lottery with Host Cheating:", result.get_counts())

quantum_lottery_cheating()
