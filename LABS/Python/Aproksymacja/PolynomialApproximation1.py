import numpy as np
import sympy as sp

# Dane wejściowe
x_vals = np.array([0, 3, 6, 9, 12])
y_vals = np.array([4, 5, 4, 1, 2])

# Definicja symbolu
x = sp.symbols('x')

# Stopień wielomianu
m = 3

# Budowanie macierzy układu A i wektora b
A = np.vstack([x_vals**i for i in range(m+1)]).T
b = y_vals

# Rozwiązanie układu normalnego A^T * A * a = A^T * b
# Macierz normalna A^T * A
ATA = A.T @ A
# Wektor A^T * b
ATb = A.T @ b

# Rozwiązanie równania
a_coeffs = np.linalg.solve(ATA, ATb)

# Konstrukcja wielomianu aproksymującego
approx_poly = sum(a_coeffs[i] * x**i for i in range(m+1))

# Wypisanie wyniku
print(f'Wielomian aproksymujący: {sp.simplify(approx_poly)}')
