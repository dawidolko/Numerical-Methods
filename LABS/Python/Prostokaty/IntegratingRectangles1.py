from sympy import symbols, sympify

# Całkowanie numeryczne — metoda prostokątów
# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = 0.06 * x**2 + 2  # Funkcja podcałkowa, zdefiniowana symbolicznie

# Parametry całkowania
a = 1  # Dolna granica całkowania
b = 4  # Górna granica całkowania
n = 3  # Liczba podziałów (prostokątów)

# Obliczenie szerokości każdego prostokąta
h = (b - a) / n

# Obliczenie przybliżonej wartości całki metodą prostokątów
# Metoda ta używa środkowego punktu każdego z podprzedziałów do aproksymacji wartości funkcji
calka = h * sum(f_x.subs(x, a + (i + 0.5) * h) for i in range(n))

# Wypisanie wyniku
print("Wynik całki metodą prostokątów:", float(calka))
