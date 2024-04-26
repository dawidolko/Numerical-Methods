from sympy import symbols, sympify, sin, cos, pi

# Wprowadzenie i legenda
print("Program do obliczania całki numerycznej metodą prostokątów.")
print("Operacje dostępne do użycia w funkcji:")
print("  * Mnożenie: *")
print("  * Potęgowanie: **")
print("  * Funkcje trygonometryczne: sin(), cos()")
print("  * Stałe matematyczne jak pi, e itd. z biblioteki sympy")
print("\nPrzykładowa funkcja to: '0.06 * x**2 + 2'")
print("Gdzie 'x' to zmienna całkowania.")

# Zapytanie o funkcję do całkowania
input_function = input("Wprowadź funkcję do całkowania (użyj 'x' jako zmiennej): ")

# Definicja zmiennej symbolicznej i funkcji
x = symbols('x')
f_x = sympify(input_function)

# Zapytanie o granice całkowania i liczbę podziałów
a = float(input("Wprowadź dolną granicę całkowania (a): "))
b = float(input("Wprowadź górną granicę całkowania (b): "))
n = int(input("Wprowadź liczbę podziałów (n): "))

# Obliczenie szerokości każdego prostokąta
h = (b - a) / n

# Obliczenie przybliżonej wartości całki metodą prostokątów
# Używamy środkowego punktu każdego z podprzedziałów
calka = h * sum(f_x.subs(x, a + (i + 0.5) * h) for i in range(n))

# Wypisanie wyniku
print(f"Wynik całki metodą prostokątów dla funkcji '{input_function}' w przedziale od {a} do {b} przy n = {n} wynosi: {calka}")
