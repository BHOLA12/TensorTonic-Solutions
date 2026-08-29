import sympy as sp
def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    x = sp.Symbol('x')
    f=(a*(x**2))+(b*x)+c
    gradi= sp.diff(f, x)
    
    for i in range(steps):
        x0=x0-lr*float(gradi.subs(x, x0))
    return x0