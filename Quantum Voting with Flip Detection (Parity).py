def quantum_vote_cheat_detect():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(3, 3)
    qc.x(0)
    qc.x(1)

    # Cheating vote flip
    qc.x(2)

    qc.measure([0, 1, 2], [0, 1, 2])
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Quantum voting with tamper:", result.get_counts())

quantum_vote_cheat_detect()
