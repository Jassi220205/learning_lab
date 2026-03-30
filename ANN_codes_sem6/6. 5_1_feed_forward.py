import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

t = float(input("Enter threshold t: "))
alpha = float(input("Enter learning rate alpha: "))

print("Enter input vector x (x1 x2 x3):")
x = list(map(float, input().split()))

print("Enter hidden layer bias v0 (3 values):")
v0 = list(map(float, input().split()))

print("Enter hidden layer weight matrix v (3x3):")
v = []
for i in range(3):
    v.append(list(map(float, input().split())))

w0 = float(input("Enter output layer bias w0: "))

print("Enter output layer weights w (3 values):")
w = list(map(float, input().split()))

Z = []

for j in range(3):
    z = v0[j]
    for i in range(3):
        z += x[i] * v[i][j]
    Z.append(sigmoid(z))

yin = w0
for j in range(3):
    yin += Z[j] * w[j]

y = sigmoid(yin)

error = t - y

print("\nHidden layer outputs:")
for i in range(3):
    print(f"Z{i+1} = {Z[i]:.4f}")

print("\nFinal output:")
print(f"y = {y:.4f}")

if y != t:
    print(f"Error (t - y) = {error:.4f}")
if y > t:
    print("Output > threshold → Neuron fires (1)")
else:
    print("Output ≤ threshold → Neuron does not fire (0)")
0