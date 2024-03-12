def bisekcja(func, a, b, error_accept):
    # Definicja funkcji lokalnej, która pozwoli na obliczanie wartości funkcji dla danego argumentu.
    def f(x):
        return func(x)
    # Sprawdzenie warunku bisekcji - funkcja musi zmieniać znak między a i b.
    if f(a) * f(b) >= 0:
        raise ValueError("Założenia bisekcji nie zostały spełnione - f(a) i f(b) muszą mieć różne znaki.")
    # Rozpoczęcie pętli bisekcji - wykonuj dopóki różnica między a i b jest większa niż akceptowalny błąd.
    while abs(b - a) > error_accept:
        # Obliczenie punktu środkowego c.
        c = (a + b) / 2
        # Jeśli f(c) == 0, to znaleziono dokładny pierwiastek, więc można przerwać pętlę.
        if f(c) == 0:
            break
        # Jeśli f(a) * f(c) < 0, to znaczy że pierwiastek znajduje się między a i c, więc nowe b to c.
        elif f(a) * f(c) < 0:
            b = c
        # W przeciwnym razie pierwiastek znajduje się między c i b, więc nowe a to c.
        else:
            a = c
    # Zwrócenie przybliżonego pierwiastka, który jest średnią arytmetyczną a i b.
    return (a + b) / 2

# Przykład użycia z funkcją lambda
try:
    # Wywołanie funkcji bisekcji z funkcją lambda x: x**3+x-1, przedziałem 0 do 1 i akceptowalnym błędem 0.01.
    root = bisekcja(lambda x: x**3+x-1, 0, 1, 0.01)
    # Wyświetlenie przybliżonego pierwiastka.
    print(f"Przybliżony pierwiastek to: {root}")
except ValueError:
    # Obsługa błędu w przypadku nie spełnienia założeń bisekcji.
    print("Założenia nie zostały spełnione")