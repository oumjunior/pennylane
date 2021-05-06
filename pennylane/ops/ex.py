import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit(params):
    qml.PauliX(0)
    qml.ops.qubit.CGeneralGate(*params, wires=[0,1])
    return qml.expval(qml.PauliZ(1))

params = np.array([0.5,0.0,np.pi,0.0])
print(circuit(params))
grad_fn = qml.grad(circuit)
print(grad_fn(params))