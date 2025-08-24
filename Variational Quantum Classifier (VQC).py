from qiskit.circuit.library import RealAmplitudes
from qiskit_machine_learning.algorithms.classifiers import VQC
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit.utils import QuantumInstance
from qiskit import Aer

feature_dim = 2
ansatz = RealAmplitudes(feature_dim, reps=1)
quantum_instance = QuantumInstance(Aer.get_backend('statevector_simulator'))

vqc = VQC(feature_map=ZZFeatureMap(feature_dim),
          ansatz=ansatz,
          optimizer=None,
          quantum_instance=quantum_instance)

print("VQC ready to train with dataset!")
