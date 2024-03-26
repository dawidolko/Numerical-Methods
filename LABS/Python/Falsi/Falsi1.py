from sympy import symbols, cos, sympify
import matplotlib.pyplot as plt

# Instrukcja dla użytkownika
print("Wprowadź swoje równanie. Użyj 'x' jako zmiennej. Przykład: '3*x - cos(x) - 1'")
equation_input = input("Podaj równanie f(x)= ")
f_x = sympify(equation_input, evaluate=False)  # Konwersja wprowadzonego równania na wyrażenie sympy

# Pobranie danych od użytkownika
a = float(input("Podaj początek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
blad = float(input("Podaj dokładność E (np. 0.00001): "))

x = symbols('x')

# Inicjalizacja listy do zapisu liczby iteracji dla różnych wartości dokładności
iteracje_dla_dokladnosci = []

# Pętla dla różnych wartości E, aby pokazać jak dokładność wpływa na liczbę iteracji
for blad in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
    if f_x.subs(x, a) * f_x.subs(x, b) >= 0:
        print(f"\nDla E={blad}: Równanie nie zawiera pierwiastka w podanym przedziale.")
    else:
        ilosc_iteracji = 0
        a_temp = a
        b_temp = b
        while True:
            f_a = f_x.subs(x, a_temp)
            f_b = f_x.subs(x, b_temp)
            x_n = a_temp - (f_a * (b_temp - a_temp)) / (f_b - f_a)  # Nowe przybliżenie korzenia

            if abs(f_x.subs(x, x_n)) < blad:
                break

            if f_a * f_x.subs(x, x_n) > 0:
                a_temp = x_n
            else:
                b_temp = x_n

            ilosc_iteracji += 1

        print(f"Dla E={blad}: Przybliżone rozwiązanie wynosi: {x_n.evalf()}, ilość iteracji: {ilosc_iteracji}")
        iteracje_dla_dokladnosci.append(ilosc_iteracji)

# Tworzenie histogramu
plt.figure(figsize=(10, 6))
plt.bar(['0.1', '0.01', '0.001', '0.0001', '0.00001'], iteracje_dla_dokladnosci, color='skyblue')
plt.xlabel('Dokładność E')
plt.ylabel('Liczba iteracji')
plt.title('Histogram liczby iteracji w zależności od dokładności E')
plt.show()
