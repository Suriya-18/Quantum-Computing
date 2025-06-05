from qiskit import Aer, QuantumCircuit, execute
from qiskit.providers.aer import AerSimulator
from qiskit.aqua.algorithms import Grover
from qiskit.aqua.components.oracles import TruthTableOracle

# Define the oracle using a truth table (e.g., for a 2-bit search space)
oracle = TruthTableOracle('101')  # This will mark '01' as the solution

# Grover's algorithm setup
grover = Grover(oracle)

# Use the AerSimulator backend
simulator = AerSimulator()

# Execute the Grover algorithm
result = grover.run(simulator)

# Output the result
print("Grover's algorithm result:", result['result'])
