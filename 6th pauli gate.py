import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer


def run_and_print(circuit, title):
    backend = Aer.get_backend("qasm_simulator")
    tqc = transpile(circuit, backend)
    job = backend.run(tqc, shots=1024)
    result = job.result()
    print(title)
    print(circuit.draw(output="text"))
    print("Result:", result.get_counts())
    print()


#  Pauli-X gate
qc_x = QuantumCircuit(1, 1)
qc_x.x(0)
qc_x.measure(0, 0)

run_and_print(qc_x, "Pauli-X Gate")


# Pauli-Y gate 
qc_y = QuantumCircuit(1, 1)
qc_y.y(0)
qc_y.measure(0, 0)

run_and_print(qc_y, "Pauli-Y Gate")


# Pauli-Z gate
qc_z = QuantumCircuit(1, 1)
qc_z.z(0)
qc_z.measure(0, 0)

run_and_print(qc_z, "Pauli-Z Gate")
