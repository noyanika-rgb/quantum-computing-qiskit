import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create circuit with 2 qubits and 1 classical bit
qc = QuantumCircuit(2,1)

# Initialize second qubit to |1>
qc.x(1)

# Apply Hadamard gates
qc.h(0)
qc.h(1)

# Oracle for balanced function (CNOT)
qc.cx(0,1)

# Apply Hadamard again
qc.h(0)

# Measure first qubit
qc.measure(0,0)

print("Quantum Circuit:")
print(qc.draw(output="text"))

# Run simulator
backend = Aer.get_backend("qasm_simulator")

compiled = transpile(qc, backend)

job = backend.run(compiled, shots=1024)

result = job.result()

print("Measurement Results:")
print(result.get_counts())
