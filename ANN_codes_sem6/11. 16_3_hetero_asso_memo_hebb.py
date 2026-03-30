import numpy as np

# Input vectors
s = list(map(int, input("Enter input pattern s: ").split()))
t = list(map(int, input("Enter target pattern t: ").split()))

s = np.array(s)
t = np.array(t)

n = len(s)
m = len(t)

# Weight matrix
T = np.zeros((n, m), dtype=int)

# Hebbian learning rule
for i in range(n):
    for j in range(m):
        T[i][j] = s[i] * t[j]

print("\nWeight Matrix (T):")
print(T)