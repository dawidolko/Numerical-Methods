from sympy import symbols, solve

# Definicja zmiennej symbolicznej i funkcji f(x)
x = symbols('x')
f_x = x**3 + x**2 - 3 * x - 3

# Parametry zadania: dokładność E oraz przedział [1, 2]
blad = 0.1  # Dokładność E
wartosc_a = 1  # Początek przedziału
wartosc_b = 2  # Koniec przedziału

# Sprawdzenie, czy funkcja spełnia warunek na obecność pierwiastka w przedziale
if f_x.subs(x, wartosc_a) * f_x.subs(x, wartosc_b) >= 0:
    print("\nRównanie f(x) nie zawiera pierwiastka równania w podanym przedziale.")
else:
    print("\nRównanie f(x) zawiera pierwiastek równania w podanym przedziale.")
    x_n = wartosc_a  # Przypisanie początkowych wartości dla metody siecznych
    x_n1 = wartosc_b

    ilosc_iteracji = 1
    while True:
        # Obliczanie kolejnych przybliżeń korzenia metodą siecznych
        f_x_n = f_x.subs(x, x_n)
        f_x_n1 = f_x.subs(x, x_n1)
        x_next = x_n1 - (f_x_n1 * (x_n1 - x_n)) / (f_x_n1 - f_x_n)

        # Warunek zakończenia iteracji: osiągnięcie zadanej dokładności
        if abs(x_next - x_n1) < blad:
            break

        # Przygotowanie do kolejnej iteracji
        x_n = x_n1
        x_n1 = x_next
        ilosc_iteracji += 1

    # Wyświetlenie wyników
    print("Ilość iteracji:", ilosc_iteracji)
    print("Przybliżone rozwiązanie równania wynosi:", x_n1.evalf())
