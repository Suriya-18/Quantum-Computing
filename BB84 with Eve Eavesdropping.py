def bb84_with_eavesdropper():
    import random
    from qiskit import QuantumCircuit, Aer, execute

    n = 8
    alice_bits = [random.randint(0, 1) for _ in range(n)]
    alice_bases = [random.choice(['Z', 'X']) for _ in range(n)]
    bob_bases = [random.choice(['Z', 'X']) for _ in range(n)]
    eve_bases = [random.choice(['Z', 'X']) for _ in range(n)]

    key = []
    eve_detection = []

    for i in range(n):
        qc = QuantumCircuit(1, 1)

        # Alice encodes
        if alice_bits[i] == 1:
            qc.x(0)
        if alice_bases[i] == 'X':
            qc.h(0)

        # Eve intercepts
        if eve_bases[i] == 'X':
            qc.h(0)
        qc.measure(0, 0)
        eve_result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1, memory=True).result().get_memory()[0]

        # Eve prepares again
        qc = QuantumCircuit(1, 1)
        if eve_result == '1':
            qc.x(0)
        if eve_bases[i] == 'X':
            qc.h(0)

        # Bob measures
        if bob_bases[i] == 'X':
            qc.h(0)
        qc.measure(0, 0)
        bob_result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1, memory=True).result().get_memory()[0]

        # Compare bases
        if alice_bases[i] == bob_bases[i]:
            key.append(int(bob_result))
            eve_detection.append(alice_bits[i] != int(bob_result))

    print(f"Shared key: {key}")
    print(f"Eavesdropping detected in {sum(eve_detection)} out of {len(eve_detection)} key bits")

bb84_with_eavesdropper()
