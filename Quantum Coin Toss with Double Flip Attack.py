def double_flip_attack():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(1, 1)
    qc.h(0)

    qc.x(0)
    qc.x(0)  # No real effect, but simulates suspicious ops

    qc.measure(0, 0)
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Double flip coin toss result:", result.get_counts())

double_flip_attack()
