def fingerprint_cheating():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(1, 1)
    qc.x(0)  # Legit fingerprint is |1>
    qc.h(0)  # Cheater changes fingerprint to |+>

    qc.measure(0, 0)
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Fingerprint check (cheating):", result.get_counts())

fingerprint_cheating()
