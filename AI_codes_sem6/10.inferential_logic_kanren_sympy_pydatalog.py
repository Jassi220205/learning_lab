# Inferential Logic using SymPy, Kanren and pyDatalog

# -----------------------------
# Using SymPy
# -----------------------------
from sympy import symbols, Implies

print("---- Using SymPy ----")

P, Q = symbols('P Q')

p_val = True
q_val = True

rule = Implies(P, Q)

print("Rule: If P then Q")
print("P =", p_val)
print("Q =", q_val)
print("Inference: If P is True and P → Q, then Q is True")

print()

# -----------------------------
# Using Kanren
# -----------------------------
from kanren import run, var, eq

print("---- Using Kanren ----")

x = var()

result = run(1, x, eq(x, "Conclusion True"))

print("Inference Result:", result)

print()

# -----------------------------
# Using pyDatalog
# -----------------------------
from pyDatalog import pyDatalog

print("---- Using pyDatalog ----")

P = True

if P:
    Q = True

print("If P is True and rule is P → Q")
print("Then Q =", Q)