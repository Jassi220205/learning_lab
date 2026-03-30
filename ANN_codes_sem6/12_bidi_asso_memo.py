import numpy as np

# Number of pattern pairs
n = int(input("Enter number of pattern pairs: "))

W = None  # Initialize weight matrix

for i in range(n):
    print(f"\nPattern pair {i+1}")
    
    # Input S and T
    S = list(map(int, input("Enter S vector (space-separated): ").split()))
    T = list(map(int, input("Enter T vector (space-separated): ").split()))
    
    # Convert to numpy arrays
    S = np.array(S)
    T = np.array(T)
    
    # Reshape for outer product
    S_row = S.reshape(1, -1)
    T_col = T.reshape(-1, 1)
    
    # Outer product
    W_i = np.dot(T_col, S_row)
    
    # Add to total weight matrix
    if W is None:
        W = W_i
    else:
        W = W + W_i

# Display final weight matrix
print("\nFinal Weight Matrix W:")
print(W)

