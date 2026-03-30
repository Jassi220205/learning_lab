import numpy as np

def hebbian_weights(X, Y):
    w = np.sum(X * Y.reshape(-1, 1), axis=0)
    w0 = np.sum(Y)
    return w, w0

# Bipolar truth tables
AND_X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]])
AND_Y = np.array([-1, -1, -1, 1])

OR_X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]])
OR_Y = np.array([-1, 1, 1, 1])

NAND_X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]])
NAND_Y = np.array([1, 1, 1, -1])

NOR_X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]])
NOR_Y = np.array([1, -1, -1, -1])

XOR_X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]])
XOR_Y = np.array([-1, 1, 1, -1])

NOT_X = np.array([[-1], [1]])
NOT_Y = np.array([1, -1])

# Calculate weights
gates = {
    "AND": (AND_X, AND_Y),
    "OR": (OR_X, OR_Y),
    "NAND": (NAND_X, NAND_Y),
    "NOR": (NOR_X, NOR_Y),
    "XOR": (XOR_X, XOR_Y),
    "NOT": (NOT_X, NOT_Y)
}

print("GATES  w1   w2   w0")
for name, (X, Y) in gates.items():
    w, w0 = hebbian_weights(X, Y)

    # Formatting for NOT (only 1 weight)
    if X.shape[1] == 1:
        print(f"{name:<5} {w[0]:>3}      {w0:>3}")
    else:
        print(f"{name:<5} {w[0]:>3}  {w[1]:>3}  {w0:>3}")
