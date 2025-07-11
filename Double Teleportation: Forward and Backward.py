def double_teleportation():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(6, 6)

    # Forward: qubit 0 to qubit 2
    qc.x(0)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.x(2).c_if(qc.cregs[0], 1)
    qc.z(2).c_if(qc.cregs[0], 2)

    # Backward: qubit 2 to qubit 5
    qc.h(3)
    qc.cx(3, 4)
    qc.cx(2, 3)
    qc.h(2)
    qc.measure([2, 3], [2, 3])
    qc.x(5).c_if(qc.cregs[0], 4)
    qc.z(5).c_if(qc.cregs[0], 8)

    qc.measure(5, 5)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Double teleportation result:", result.get_counts())

double_teleportation()
