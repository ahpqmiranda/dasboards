import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x, y = sp.symbols('x y')

y = sp.sin(x) + sp.log(x**2)

print(y.subs(x, 5))
