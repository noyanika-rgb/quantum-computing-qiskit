from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(2,1)

qc.x(1)
qc.h(0)
qc.h(1)

qc.cx(0,1)

qc.h(0)

qc.measure(0,0)

backend = Aer.get_backend('qasm_simulator')
job = backend.run(transpile(qc, backend), shots=1024)

result = job.result()
print(result.get_counts())