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

# === Vector Operations ===

add = v1 + v2
sub = v1 - v2
dot = np.dot(v1, v2)
mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)

# Angle between vectors (in degrees)
cos_theta = dot / (mag_v1 * mag_v2)
angle = np.degrees(np.arccos(cos_theta))

print("\nVector Operations:")
print("v1 + v2 =", add)
print("v1 - v2 =", sub)
print("Dot Product =", dot)
print("Magnitude of v1 =", mag_v1)
print("Magnitude of v2 =", mag_v2)
print("Angle between v1 & v2 =", angle, "degrees")

# --- Plotting vectors ---
plt.figure(figsize=(6, 6))
origin = [0, 0]

# Original vectors
plt.quiver(*origin, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(*origin, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red')

# Resultant vector (addition)
plt.quiver(*origin, add[0], add[1], angles='xy', scale_units='xy', scale=1, color='green')

plt.xlim(-2, 6)
plt.ylim(-3, 6)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Vector Operations Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["v1", "v2", "v1 + v2"])
plt.show()