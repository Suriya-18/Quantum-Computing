from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def qft(n):
    qc = QuantumCircuit(n)
    for i in range(n):
        qc.h(i)
        for j in range(i+1, n):
            qc.cp(np.pi/2**(j-i), j, i)
    qc.reverse_bits()
    return qc

qc = qft(3)
qc.draw('mpl')

backend = Aer.get_backend('unitary_simulator')
result = execute(qc, backend).result()
unitary = result.get_unitary()
print("QFT unitary matrix:\n", unitary)
