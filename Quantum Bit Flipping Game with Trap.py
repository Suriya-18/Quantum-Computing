def bit_flip_trap():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)

    # Bob flips
    qc.x(0)

    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Bit flip with trap result:", result.get_counts())

bit_flip_trap()

