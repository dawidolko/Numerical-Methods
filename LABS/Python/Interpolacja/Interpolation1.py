# Import biblioteki sympy
import sympy as sp

# Definicja punktów jako lista krotek (x, y)
points = [(1, 5), (2, 7), (3, 6)]

# Rozpakowanie współrzędnych do oddzielnych list x_vals i y_vals
x_vals, y_vals = zip(*points)

# Tworzenie symbolu x do obliczeń algebraicznych
x = sp.symbols('x')


# Funkcja wykonująca interpolację metodą Lagrange'a
def lagrange_interpolation(x_vals, y_vals):
    n = len(x_vals)  # Liczba punktów
    L = 0  # Wielomian Lagrange'a inicjalizowany jako 0
    for i in range(n):
        li = y_vals[i]  # Rozpoczynamy od wartości y_i
        for j in range(n):
            if i != j:
                # Mnożymy przez odpowiednie ułamki tworzące bazę Lagrange'a
                li *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        L += li  # Dodajemy składnik do wielomianu
    return sp.simplify(L)  # Uproszczenie wyniku


# Funkcja wykonująca interpolację metodą Newtona
def newton_interpolation(x_vals, y_vals):
    # Funkcja wewnętrzna obliczająca współczynniki podzielonych różnic
    def divided_diff(x_vals, y_vals):
        n = len(x_vals)
        coef = [y for y in y_vals]
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                # Obliczanie podzielonych różnic
                coef[i] = (coef[i] - coef[i - 1]) / (x_vals[i] - x_vals[i - j])
        return coef

    coef = divided_diff(x_vals, y_vals)
    n = len(coef)
    N = coef[0]  # Początkowa wartość to f[x_0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_vals[j])  # Mnożymy przez odpowiednie iloczyny (x - x_j)
        N += term  # Dodajemy do wielomianu
    return sp.simplify(N)  # Uproszczenie wyniku


# Obliczenie wielomianów interpolacyjnych dla obu metod
L = lagrange_interpolation(x_vals, y_vals)
N = newton_interpolation(x_vals, y_vals)

# Wyświetlenie wyników
print(f'Interpolacja Lagrange\'a: {L}')
print(f'Interpolacja Newtona: {N}')
