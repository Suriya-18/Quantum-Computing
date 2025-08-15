from qiskit.algorithms import QAOA
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit import Aer
import numpy as np

# Create a sample optimization problem
qp = QuadraticProgram()
qp.binary_var('x0')
qp.binary_var('x1')
qp.maximize(linear=[1, 2], quadratic={(0, 1): 1})

# QAOA with AI optimizer- COBYLA
backend = Aer.get_backend('statevector_simulator')
qaoa = QAOA(optimizer='COBYLA', reps=1, quantum_instance=backend)

optimizer = MinimumEigenOptimizer(qaoa)
result = optimizer.solve(qp)

print(result)
