from qiskit import QuantumCircuit, Aer, execute
from sklearn.svm import SVC

def encode_data(x):
    qc = QuantumCircuit(1)
    qc.ry(x*np.pi, 0)
    qc.measure_all()
    return qc

backend = Aer.get_backend('qasm_simulator')
data = [0.1, 0.3, 0.8, 0.9]
labels = [0, 0, 1, 1]

features = []
for x in data:
    qc = encode_data(x)
    job = execute(qc, backend, shots=1024)
    counts = job.result().get_counts()
    prob_1 = counts.get('1', 0)/1024
    features.append([prob_1])

clf = SVC(kernel='linear')
clf.fit(features, labels)
print("Prediction for 0.4:", clf.predict([[0.4]]))
