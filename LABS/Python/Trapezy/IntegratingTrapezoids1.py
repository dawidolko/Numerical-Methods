import sympy as sp  # Import biblioteki sympy do pracy z matematyką symboliczną


def trapezoidal_rule(f, a, b, n):
    """
    Funkcja obliczająca całkę numeryczną metodą trapezów.
    :param f: funkcja podcałkowa
    :param a: dolna granica całkowania
    :param b: górna granica całkowania
    :param n: liczba podziałów przedziału (liczba trapezów)
    :return: przybliżona wartość całki
    """
    x = sp.symbols('x')  # Definicja symbolu x
    h = (b - a) / n  # Obliczenie kroku h

    # Tworzenie punktów xi w przedziale [a, b]
    xi_values = [a + i * h for i in range(n + 1)]

    # Obliczenie sumy wartości funkcji f w punktach xi
    sum_fx = sum(f.subs(x, xi) for xi in xi_values[1:-1])

    # Aplikacja wzoru na metodę trapezów
    integral_approx = h / 2 * (f.subs(x, a) + 2 * sum_fx + f.subs(x, b))

    return integral_approx.evalf()  # Zwrócenie wartości numerycznej wyniku


# Funkcja podcałkowa sqrt(1+x)
f = sp.sqrt(1 + sp.symbols('x'))

# Ustawienia dla obliczenia całki
a = 0  # Dolna granica całkowania
b = 1  # Górna granica całkowania
n = 3  # Liczba podziałów (krok h = 1/3)

# Wywołanie funkcji do obliczenia całki i wypisanie wyniku
result = trapezoidal_rule(f, a, b, n)
print("Przybliżona wartość całki to:", result)
