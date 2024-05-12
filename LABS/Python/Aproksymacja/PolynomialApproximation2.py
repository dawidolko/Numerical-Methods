import numpy as np
import sympy as sp

# Definicja symbolu x
x = sp.symbols('x')

# Dane wejściowe
x_vals = np.array([0, 3, 6, 9, 12])
y_vals = np.array([4, 5, 4, 1, 2])

# Stopień wielomianu
m = 3

# Tworzenie macierzy Vandermonde'a dla wielomianu stopnia m
A = np.vander(x_vals, m+1, increasing=True)

# Rozwiązanie układu równań metodą najmniejszych kwadratów (np.linalg.lstsq)
coeffs, residuals, rank, s = np.linalg.lstsq(A, y_vals, rcond=None)

# Tworzenie wielomianu aproksymacyjnego
approx_poly = sum(coeffs[i] * x**i for i in range(m+1))

# Wyświetlanie wyników
print("Współczynniki wielomianu:", coeffs)
print("Wielomian aproksymujący:", sp.simplify(approx_poly))
