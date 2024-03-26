from sympy import symbols, cos

# Rozwiązywanie równania nieliniowego 3x - cos(x) - 1 = 0 metodą falsi w przedziale [0.25, 0.75] z dokładnością E=0.00001

x = symbols('x')
f_x = 3 * x - cos(x) - 1  # Definicja funkcji f(x)

# Parametry początkowe
blad = 0.00001  # Dokładność E
a = 0.25  # Początek przedziału
b = 0.75  # Koniec przedziału

# Sprawdzenie, czy w podanym przedziale istnieje pierwiastek
if f_x.subs(x, a) * f_x.subs(x, b) >= 0:
    print("\nRównanie f(x) nie zawiera pierwiastka w podanym przedziale.")
else:
    print("\nRównanie f(x) zawiera pierwiastek w podanym przedziale.")

    ilosc_iteracji = 0
    while True:
        f_a = f_x.subs(x, a)
        f_b = f_x.subs(x, b)
        x_n = a - (f_a * (b - a)) / (f_b - f_a)  # Obliczanie nowego przybliżenia korzenia
        wartosc_f_x_n = f_x.subs(x, x_n)

        # Sprawdzenie, czy osiągnięto wymaganą dokładność
        if abs(wartosc_f_x_n) < blad:
            break

        # Aktualizacja przedziału
        if f_a * wartosc_f_x_n > 0:
            a = x_n
        else:
            b = x_n

        ilosc_iteracji += 1

    # Wyniki
    print(f"Ilość iteracji: {ilosc_iteracji}")
    print(f"Przybliżone rozwiązanie równania wynosi: {x_n.evalf()}")
