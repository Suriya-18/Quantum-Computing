from qiskit.algorithms import QAOA
from qiskit_optimization.applications import Maxcut
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization import QuadraticProgram
from qiskit.circuit.library import TwoLocal
from qiskit import Aer
import networkx as nx

# Create a simple MaxCut problem
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
maxcut = Maxcut(G)
problem = maxcut.to_quadratic_program()

# Convert to QUBO
qubo = QuadraticProgramToQubo().convert(problem)

# QAOA Solver
qaoa = QAOA(optimizer=COBYLA(), quantum_instance=Aer.get_backend('aer_simulator'))
optimizer = MinimumEigenOptimizer(qaoa)

result = optimizer.solve(qubo)
print("MaxCut solution:", result)
