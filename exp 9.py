import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create quantum circuit
qc = QuantumCircuit(1,1)
# Create superposition
qc.h(0)
# Measure the qubit
qc.measure(0,0)

print("Quantum Circuit:")
print(qc.draw(output="text"))

# Run the circuit on simulator
backend = Aer.get_backend("qasm_simulator")

compiled_circuit = transpile(qc, backend)

job = backend.run(compiled_circuit, shots=1024)

result = job.result()
# Display measurement results
counts = result.get_counts()

print("Measurement Results:")
print(counts)
