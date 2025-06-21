def dishonest_secret_sharing():
    qc = QuantumCircuit(3, 3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Charlie is dishonest: refuses to cooperate
    # Bob and Charlie should both measure in X-basis, but Charlie skips
    qc.h(1)
    qc.measure([0, 1, 2], [0, 1, 2])

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    counts = result.get_counts()
    print("Secret Sharing (Charlie dishonest):", counts)

dishonest_secret_sharing()
