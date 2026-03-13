import numpy as np
import matplotlib.pyplot as plt

# --- Scalars ---
a = 5
b = 12.3

print("Scalars:")
print("a =", a)
print("b =", b)

# --- Vectors ---
v1 = np.array([2, 3])
v2 = np.array([4, -1])

print("\nVectors:")
print("v1 =", v1)
print("v2 =", v2)

# --- Plotting vectors ---
plt.figure(figsize=(6, 6))
origin = [0, 0]

# Plot v1
plt.quiver(*origin, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')

# Plot v2
plt.quiver(*origin, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')

plt.xlim(-2, 6)
plt.ylim(-3, 5)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Vector Display")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["v1", "v2"])
plt.show()