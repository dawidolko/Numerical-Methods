from sympy import symbols, sin, cos, pi, sympify, diff
from sympy.plotting import plot

# Instrukcje dla użytkownika, jak wprowadzać dane
print("Wprowadź swoje równanie. Użyj następujących oznaczeń:")
print("* dla mnożenia, ** dla potęgowania, pi dla liczby Pi, np. sin(x) * pi ** 2")
print("Przykład równania: x**3 + x**2 - 3*x - 3")

# Wprowadzanie równania przez użytkownika
x = symbols('x')
equation_input = input("Podaj równanie: ")
f_x = sympify(equation_input)

# Wprowadzanie przedziału i dokładności E przez użytkownika
a = float(input("Podaj początek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
blad = float(input("Podaj dokładność E (np. 0.1): "))

# Metoda siecznych
x_n = a
x_n1 = b
counter = 0

while True:
    f_x_n = f_x.subs(x, x_n)
    f_x_n1 = f_x.subs(x, x_n1)
    x_next = x_n1 - (f_x_n1 * (x_n1 - x_n)) / (f_x_n1 - f_x_n)

    if abs(x_next - x_n1) < blad:
        break

    x_n = x_n1
    x_n1 = x_next
    counter += 1

print(f"Ilość iteracji: {counter}")
print(f"Przybliżone rozwiązanie równania wynosi: {x_n1.evalf()}")

# Tutaj dodatkowy kod do generowania histogramu zostanie pominięty,
# ponieważ wymagałby bardziej skomplikowanego podejścia i zrozumienia, co dokładnie ma być przedstawione.
