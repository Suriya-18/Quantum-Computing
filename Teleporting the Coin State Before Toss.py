def teleport_and_toss():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(3, 3)
    qc.h(0)  # Prepare fair coin

    # Entangle qubits 1 & 2
    qc.h(1)
    qc.cx(1, 2)

    # Teleport qubit 0 to qubit 2
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.x(2).c_if(qc.cregs[0], 1)
    qc.z(2).c_if(qc.cregs[0], 2)

    # Measure teleported coin
    qc.measure(2, 2)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
    print("Teleportation Toss Result:", result)

teleport_and_toss()
