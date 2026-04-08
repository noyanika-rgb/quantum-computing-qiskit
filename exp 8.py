import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1,1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Measure the qubit
qc.measure(0,0)
# Draw the circuit
print("Quantum Circuit:")
print(qc.draw(output="text"))
# Run the circuit on simulator
backend = Aer.get_backend("qasm_simulator")

compiled_circuit = transpile(qc, backend)

job = backend.run(compiled_circuit, shots=1024)

result = job.result()
# Print results
print("Measurement Results:")
print(result.get_counts())
