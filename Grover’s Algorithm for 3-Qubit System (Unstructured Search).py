from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import GroverOperator
from qiskit.algorithms import Grover
from qiskit.algorithms.optimizers import SPSA
from qiskit.circuit.library import PhaseOracle

oracle = PhaseOracle("a & b & c")
grover = Grover(oracle=oracle)
result = grover.run()
print("Result:", result)
