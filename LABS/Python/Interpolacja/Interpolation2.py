import sympy as sp

def lagrange_symbolic(x1, y1, x2, y2, x3, y3):
    x = sp.symbols('x')
    w1 = y1*(x-x2)*(x-x3)/((x1-x2)*(x1-x3))
    w2 = y2*(x-x1)*(x-x3)/((x2-x1)*(x2-x3))
    w3 = y3*(x-x1)*(x-x2)/((x3-x1)*(x3-x2))

    lagrange_polynomial = w1 + w2 + w3
    return sp.simplify(lagrange_polynomial)

# Wywołanie funkcji z danymi punktami
print(lagrange_symbolic(1, 5, 2, 7, 3, 6))
