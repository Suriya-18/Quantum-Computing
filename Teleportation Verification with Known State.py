def teleport_and_verify():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(3, 3)
    qc.x(0)  # Teleport |1⟩

    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.x(2).c_if(qc.cregs[0], 1)
    qc.z(2).c_if(qc.cregs[0], 2)

    qc.measure(2, 2)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Teleport |1⟩ verification:", result.get_counts())

teleport_and_verify()
