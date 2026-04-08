import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
# Create quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2,2)
# Apply Hadamard gate
qc.h(0)
# Apply CNOT gate
qc.cx(0,1)
# Measure both qubits
qc.measure([0,1], [0,1])

print("Quantum Circuit:")
print(qc.draw(output="text"))
# Run on simulator
backend = Aer.get_backend("qasm_simulator")

compiled_circuit = transpile(qc, backend)

job = backend.run(compiled_circuit, shots=1024)

result = job.result()
# Display results
counts = result.get_counts()

print("Measurement Results:")
print(counts)


