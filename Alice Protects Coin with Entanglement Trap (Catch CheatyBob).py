from qiskit import QuantumRegister

def entangled_coin_protection():
    qreg = QuantumRegister(2)  # coin[0], trap[1]
    qc = QuantumCircuit(qreg, 2)

    # Step 1: Create Bell state between coin and trap
    qc.h(0)
    qc.cx(0, 1)

    print("Alice: Coin entangled with a trap qubit...")

    # Step 2: Bob tampers with the coin (applies X)
    qc.x(0)
    print("Bob: Tried to flip the coin...")

    # Step 3: Alice reverses Bell and checks for disturbance
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    
    print("Detection Result:", counts)
    plot_histogram(counts).show()

entangled_coin_protection()
