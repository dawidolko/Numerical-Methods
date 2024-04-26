from sympy import symbols, sympify, diff, exp, sin, integrate

# Legenda dla użytkownika
print("Witaj w programie do całkowania metodą Simpsona!")
print("Możesz wprowadzić funkcję używając standardowej składni matematycznej.")
print("Przykłady:")
print("  * Mnożenie: * (np. x*2)")
print("  * Dzielenie: / (np. x/2)")
print("  * Potęgowanie: ** (np. x**2)")
print("  * Funkcje trygonometryczne: sin(), cos(), exp() (np. sin(x), exp(x))")
print("  * Liczba e: E (np. exp(1) == E)")
print("Pamiętaj, aby zmienną całkowania oznaczyć jako 'x'.")

# Wprowadzenie danych przez użytkownika
input_function = input("Wprowadź funkcję do całkowania: ")
a = float(input("Wprowadź dolną granicę całkowania (a): "))
b = float(input("Wprowadź górną granicę całkowania (b): "))
n = int(input("Wprowadź liczbę podziałów (n): "))

# Weryfikacja czy n jest parzyste
if n % 2 != 0:
    raise ValueError("Liczba podziałów (n) musi być parzysta dla metody Simpsona.")

# Definicja symboli i funkcji
x = symbols('x')
f_x = sympify(input_function)  # Przekształcenie wprowadzonego ciągu znaków na wyrażenie sympy

# Szerokość każdego przedziału
h = (b - a) / n

# Obliczenie całki metodą Simpsona
calka = h / 3 * (f_x.subs(x, a) + 4 * sum(f_x.subs(x, a + i * h) for i in range(1, n, 2)) + \
                  2 * sum(f_x.subs(x, a + i * h) for i in range(2, n, 2)) + f_x.subs(x, b))

# Obliczenie błędu oszacowania
f_x_pochodna4 = diff(f_x, x, 4)
max_f_x_pochodna4 = max(abs(f_x_pochodna4.subs(x, xi)) for xi in [a, (a + b) / 2, b])
blad = (h**4 / 180) * (b - a) * max_f_x_pochodna4

# Wypisanie wyniku
print(f"Wynik całki metodą Simpsona: {calka.evalf()}")
print(f"Szacowany błąd metody: {blad.evalf()}")

# Obliczenie całki dokładnie dla porównania (jeśli jest to możliwe)
try:
    calka_dokladna = integrate(f_x, (x, a, b))
    print(f"Dokładny wynik całki: {calka_dokladna.evalf()}")
except:
    print("Nie można obliczyć dokładnej wartości całki dla podanej funkcji.")
