import numpy as np

# Input pattern
s = list(map(int, input("Enter pattern elements separated by space: ").split()))
s = np.array(s)

n = len(s)

# Hebbian weight matrix
T = np.zeros((n, n), dtype=int)

for i in range(n):
    for j in range(n):
        T[i][j] = s[i] * s[j]

print("\nWeight Matrix (T):")
print(T)

# Row 4 as small t
t = T[3]

print("\nt =", list(t))