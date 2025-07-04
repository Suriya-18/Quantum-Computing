def teleport_and_eve_clones_input():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(4, 4)
    qc.h(0)  # Alice prepares unknown |+>

    # Eve intercepts and tries to copy
    qc.cx(0, 3)

    # Entangle 1 and 2 for teleportation
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    qc.x(2).c_if(qc.cregs[0], 1)
    qc.z(2).c_if(qc.cregs[0], 2)
    qc.measure(2, 2)
    qc.measure(3, 3)  # Eve’s copy

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Teleport + Eve clone result:", result.get_counts())

teleport_and_eve_clones_input()
