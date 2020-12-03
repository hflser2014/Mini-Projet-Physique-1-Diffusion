import matplotlib.pyplot as plt
import numpy as np
import sympy as spy
from IPython.display import display, Latex

spy.init_printing(use_unicode=True)

alphalist =np.linspace(0,6.28,100) 
def func(alpha):
    return np.sin(alpha)**2
ylist = [func(alpha) for alpha in alphalist]


r = 1.0
alpha,t = spy.symbols('alpha t')

d0 = 10

def dis(alpha):
    return spy.sqrt((d0+spy.cos(alpha)*r)**2+spy.sin(alpha)*r**2)

int1 = spy.Integral(dis(alpha)/2/spy.pi,(alpha,0,2*spy.pi))

display(Latex(f"$${spy.latex(int1)}={spy.latex(int1.doit())}={spy.latex(int1.doit().evalf())}$$"))
