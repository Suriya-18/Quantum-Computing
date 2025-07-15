def detect_cheating():
    from qiskit import QuantumCircuit, Aer, execute

    honest_qc = QuantumCircuit(1, 1)
    honest_qc.h(0)
    honest_qc.measure(0, 0)
    honest_result = execute(honest_qc, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()

    cheaty_qc = QuantumCircuit(1, 1)
    cheaty_qc.h(0)
    cheaty_qc.x(0)
    cheaty_qc.measure(0, 0)
    cheat_result = execute(cheaty_qc, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()

    print("Honest Toss Stats:", honest_result)
    print("Cheating Toss Stats:", cheat_result)

detect_cheating()
