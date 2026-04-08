import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure(0, 0)
qc.measure(1, 1)

# Force ASCII drawer
print("Quantum Circuit:")
print(qc.draw(output="text", fold=-1, cregbundle=False))

backend = Aer.get_backend("qasm_simulator")

tqc = transpile(qc, backend)
job = backend.run(tqc, shots=1024)

result = job.result()

print("Measurement Results:")
print(result.get_counts())
