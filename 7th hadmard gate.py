from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create a single qubit circuit
qc = QuantumCircuit(1)

# Apply Hadamard gate
qc.h(0)

# Get the statevector of the circuit
state = Statevector.from_instruction(qc)

# Plot Bloch sphere
fig = plot_bloch_multivector(state)

# Show the Bloch sphere
plt.show()
