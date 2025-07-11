def teleport_to_two():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(5, 5)
    qc.h(0)  # |+⟩

    # Alice entangles with Bob
    qc.h(1)
    qc.cx(1, 2)

    # Also entangles with Charlie
    qc.h(3)
    qc.cx(3, 4)

    # Teleport to Bob
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.x(2).c_if(qc.cregs[0], 1)
    qc.z(2).c_if(qc.cregs[0], 2)

    # Measure Bob & Charlie
    qc.measure([2, 4], [3, 4])
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Teleport to two recipients (entangled targets):", result.get_counts())

teleport_to_two()
