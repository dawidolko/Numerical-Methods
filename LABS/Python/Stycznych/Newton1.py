from sympy import sympify, symbols, diff, pi

# Definicja zmiennej symbolicznej
x = symbols('x')

# Instrukcje dla użytkownika, w tym jak wprowadzać 'pi'
prompt = input("Pamiętaj oznaczać:\n\t* jako mnożenie\n\t** jako potęgowanie\n\t'pi' jako π\nPodaj wzór funkcji: ")
# Konwersja podanego wzoru na obiekt wyrażenia sympy, z uwzględnieniem 'pi'
f = sympify(prompt, {"pi": pi})

# Pochodna funkcji
d1 = diff(f, x)

# Pobranie od użytkownika początku i końca przedziału, z możliwością wprowadzenia 'pi'
a_input = input("Podaj początek przedziału (możesz użyć 'pi'): ")
b_input = input("Podaj koniec przedziału (możesz użyć 'pi'): ")

# Konwersja przedziałów na wartości liczbowe lub symboliczne
a = sympify(a_input, {"pi": pi})
b = sympify(b_input, {"pi": pi})

# Sprawdzenie warunku Twierdzenia Bolzano-Cauchy'ego dla funkcji
if f.subs(x, a) * f.subs(x, b) > 0:
    print("\nTwierdzenie Bolzano-Cauchy'ego nie jest spełnione")
    print(f"W przedziale [{a}, {b}] najpewniej nie ma miejsca zerowego")
else:
    epsilon = float(input("Wybierz dokładność (epsilon): "))  # Pobranie dokładności od użytkownika

    # Wybór początkowego przybliżenia (tu: środek przedziału)
    x0 = (a + b) / 2

    # Metoda stycznych (Newtona)
    counter = 0
    while abs(f.subs(x, x0)) > epsilon:
        x0 = x0 - f.subs(x, x0)/d1.subs(x, x0)
        counter += 1

    print(f"\nFunkcja f(x) = {f}")
    print(f"ma miejsce zerowe w x = {x0.evalf()}")
    print(f"znaleziona w {counter} próbach")
