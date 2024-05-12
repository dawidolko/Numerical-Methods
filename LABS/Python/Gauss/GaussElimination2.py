import numpy as np


def gauss_elimination_with_pivoting(A, b):
    """
    Funkcja wykonuje eliminację Gaussa z częściowym wyborem elementu głównego.

    Args:
    A (np.array): Macierz współczynników układu równań (macierz kwadratowa).
    b (np.array): Wektor wyrazów wolnych.

    Returns:
    np.array: Rozwiązanie układu równań.
    """
    n = len(b)
    A = A.astype(float)  # Konwersja na liczby zmiennoprzecinkowe dla dokładności
    b = b.astype(float)

    # Przejście przez każdą kolumnę macierzy
    for i in range(n):
        # Wybór wiersza z maksymalnym elementem w i-tej kolumnie jako pivot
        max_row = np.argmax(np.abs(A[i:, i])) + i
        # Zamiana miejscami wierszy, jeśli potrzebne
        A[[i, max_row]], b[[i, max_row]] = A[[max_row, i]], b[[max_row, i]]

        # Eliminacja wszystkich elementów poniżej pivotu
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Wsteczne podstawienie do wyznaczenia wartości zmiennych
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


# Dane wejściowe: macierz A i wektor b
A = np.array([[3, 0, 6],
              [1, 2, 8],
              [4, 5, -2]])

b = np.array([-12, -12, 39])

# Rozwiązanie układu równań
x = gauss_elimination_with_pivoting(A, b)
print("Rozwiązanie x:", x)
