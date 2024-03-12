# Importowanie funkcji sympify z biblioteki sympy, która umożliwia konwersję stringów na wyrażenia sympy
from sympy import sympify

# Pobranie od użytkownika wzoru funkcji z przypomnieniem o notacji matematycznej
prompt = input("Pamiętaj oznaczać:\n\t* jako mnożenie\n\t** jako potęgowanie\nPodaj wzór funkcji: ")
# Konwersja podanego wzoru na obiekt wyrażenia sympy
f = sympify(prompt)

# Pobranie od użytkownika początku i końca przedziału analizy funkcji
a = float(input("Podaj początek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
# Wyznaczenie minimum i maksimum z podanego przedziału
min = min(a, b)
max = max(a, b)

# Sprawdzenie warunku Twierdzenia Bolzano-Cauchy'ego dla funkcji
if f.subs("x", min) * f.subs("x", max) > 0:
    # Informacja o niespełnieniu warunku twierdzenia
    print("\nTwierdzenie Bolzano-Cauchy'ego nie jest spełnione")
    print(f"W przedziale [{min}, {max}] najpewniej nie ma miejsca zerowego")
    # Zakończenie programu, jeśli warunek nie jest spełniony
    exit(1)

# Pobranie od użytkownika wartości epsilon określającej dokładność szukania miejsca zerowego
epsilon = float(input("Wybierz dokładność(epsilon): "))

# Inicjalizacja zmiennych pomocniczych do metody połowienia
temp_min = min
temp_max = max
# Wstępne obliczenie punktu środkowego przedziału
x = (temp_min+temp_max)/2
# Licznik prób znalezienia miejsca zerowego
counter = 1
# Pętla wykonująca metodę połowienia do momentu spełnienia warunku dokładności
while abs(f.subs("x", x)) > epsilon:
    x = (temp_min+temp_max)/2

    counter += 1

    # Decyzja o zmianie przedziału poszukiwań w zależności od wartości funkcji
    if f.subs("x", x) * f.subs("x", temp_min) <= 0:
        temp_max = x
    else:
        temp_min = x

# Wyświetlenie informacji o znalezionym miejscu zerowym
print(f"\nFunkcja f(x) = {f}")
print(f"ma miejsce zerowe w x = {x}")
print(f"znaleziona w {counter} próbach")
