from sympy import symbols, sin, exp, diff, integrate

# Definicja symboli i funkcji
x = symbols('x')
f_x = sin(x) * exp(-3 * x) + x**3  # Funkcja podcałkowa

# Parametry całkowania
a = -3  # Dolna granica całkowania
b = 1   # Górna granica całkowania
n = 2   # Liczba podziałów (dla jednego przedziału n=2)

# Szerokość każdego przedziału (podstawa paraboli)
h = (b - a) / n

# Obliczenie przybliżonej wartości całki metodą Simpsona dla jednego przedziału
calka = h / 3 * (f_x.subs(x, a) + 4 * f_x.subs(x, (a + b) / 2) + f_x.subs(x, b))

# Obliczenie czwartej pochodnej funkcji
f_x_pochodna4 = diff(f_x, x, 4)

# Znalezienie maksymalnej wartości czwartej pochodnej na przedziale (używamy punktów równoodległych)
max_f_x_pochodna4 = max(abs(f_x_pochodna4.subs(x, xi)) for xi in [a, (a + b) / 2, b])

# Obliczenie błędu oszacowania
blad = (h**5 / 90) * max_f_x_pochodna4

# Wypisanie wyniku
print(f"Wynik całki metodą Simpsona: {calka.evalf()}")
print(f"Szacowany błąd metody: {blad.evalf()}")

# Obliczenie całki dokładnie dla porównania
calka_dokladna = integrate(f_x, (x, a, b))
print(f"Dokładny wynik całki: {calka_dokladna.evalf()}")
