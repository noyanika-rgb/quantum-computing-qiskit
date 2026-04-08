from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# Create quantum register with 2 qubits
q = QuantumRegister(2, 'q')

# Create classical register with 2 bits
c = ClassicalRegister(2, 'c')

# Create circuit
qc = QuantumCircuit(q, c)

# Apply Hadamard gate on first qubit
qc.h(q[0])

# Measure qubits into classical bits
qc.measure(q, c)

# Run on simulator
backend = Aer.get_backend("qasm_simulator")
tqc = transpile(qc, backend)

job = backend.run(tqc, shots=1024)
result = job.result()

print("Measurement result:")
print(result.get_counts())
