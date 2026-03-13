# Propositional Logic using SymPy, Kanren and pyDatalog

# -----------------------------
# Using SymPy
# -----------------------------
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not

print("---- Using SymPy ----")

P, Q = symbols('P Q')

p_val = True
q_val = True

print("If P is", p_val, "and Q is", q_val)

result_and = And(p_val, q_val)
result_or = Or(p_val, q_val)
result_not = Not(p_val)

print("P AND Q →", result_and)
print("P OR Q →", result_or)
print("NOT P →", result_not)

print()

# -----------------------------
# Using Kanren
# -----------------------------
from kanren import run, var, eq

print("---- Using Kanren ----")

x = var()

result = run(1, x, eq(x, True))

print("If P is True then result →", result)

print()

# -----------------------------
# Using pyDatalog
# -----------------------------
from pyDatalog import pyDatalog

print("---- Using pyDatalog ----")

P = True
Q = True

result = P and Q

print("If P is", P, "and Q is", Q, "→ Result is", result)