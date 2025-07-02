def key_confirmation_tamper():
    from qiskit import QuantumCircuit, Aer, execute

    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)

    # Eve tampers with one qubit
    qc.z(1)

    qc.measure([0, 1], [0, 1])
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
    print("Key confirmation mismatch:", result.get_counts())

key_confirmation_tamper()
