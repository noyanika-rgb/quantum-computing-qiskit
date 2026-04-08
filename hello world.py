from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer  

print("Hello World from Qiskit")

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

backend = Aer.get_backend("qasm_simulator")

tqc = transpile(qc, backend)
job = backend.run(tqc, shots=1024)

result = job.result()
print(result.get_counts())

