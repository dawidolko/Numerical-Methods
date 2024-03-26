from sympy import symbols, sin, pi, diff

# Definicja zmiennej symbolicznej
x = symbols('x')

# Zdefiniowanie funkcji zgodnie z treścią zadania
f = sin(x) - 1/2 * x

# Pochodna funkcji
d1 = diff(f, x)

# Początek i koniec przedziału z treści zadania
a = pi/2
b = pi

# Sprawdzenie warunku Twierdzenia Bolzano-Cauchy'ego dla funkcji
if f.subs(x, a) * f.subs(x, b) > 0:
    print("\nTwierdzenie Bolzano-Cauchy'ego nie jest spełnione")
    print(f"W przedziale [{a}, {b}] najpewniej nie ma miejsca zerowego")
else:
    epsilon = 0.01  # Dokładność z treści zadania
    x0 = a  # Wybór początkowego przybliżenia

    # Metoda stycznych (Newtona)
    counter = 0
    while abs(f.subs(x, x0)) > epsilon:
        x0 = x0 - f.subs(x, x0)/d1.subs(x, x0)
        counter += 1

    print(f"\nFunkcja f(x) = {f}")
    print(f"ma miejsce zerowe w x = {x0.evalf()}")
    print(f"znaleziona w {counter} próbach")
