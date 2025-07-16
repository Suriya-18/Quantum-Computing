def compare_classical_quantum():
    import random
    from qiskit import QuantumCircuit, Aer, execute

    classical = [random.choice(['H', 'T']) for _ in range(1000)]

    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    quantum = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()

    print("Classical Toss:", {"H": classical.count("H"), "T": classical.count("T")})
    print("Quantum Toss:", quantum)

compare_classical_quantum()
