from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def teleport_with_cheating():
    qr = QuantumRegister(3)  # [Alice, Entangle_AliceBob, Bob]
    cr = ClassicalRegister(2)
    qc = QuantumCircuit(qr, cr)

    # Step 1: Prepare state to teleport
    qc.h(0)

    # Step 2: Entangle qubits 1 and 2 (Bell pair)
    qc.h(1)
    qc.cx(1, 2)

    # Step 3: Bell measurement on qubits 0 and 1
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], cr)

    # Bob tries to cheat by applying X before receiving classical bits
    qc.x(2)
    print("Bob: Tampering with the qubit before classical data received...")

    # Step 4: Bob’s correction (should be I, X, Z, or XZ)
    qc.barrier()
    qc.x(2).c_if(cr[1], 1)
    qc.z(2).c_if(cr[0], 1)

    # Measure the teleported qubit
    qc.measure(2, 0)

    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    print("Final (cheated teleportation) result:", counts)
    plot_histogram(counts).show()

teleport_with_cheating()
