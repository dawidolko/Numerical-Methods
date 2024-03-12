def horner(tablica, x):
    # Inicjalizacja wyniku wartością współczynnika przy najwyższej potędze.
    wynik = tablica[0]
    # Iteracja po współczynnikach wielomianu, zaczynając od współczynnika przy potędze niższej niż najwyższa.
    for i in range(1, len(tablica)):
        # Zastosowanie schematu Hornera do obliczenia wartości wielomianu dla danej wartości x.
        wynik = wynik * x + tablica[i]
    # Zwrócenie obliczonej wartości wielomianu.
    return wynik

# Pobranie stopnia wielomianu od użytkownika.
stopien_wielomianu = int(input("Podaj stopień wielomianu: "))
# Inicjalizacja pustej listy na współczynniki wielomianu.
tablica = []

# Pobranie współczynników wielomianu od użytkownika.
print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(stopien_wielomianu + 1):
    y = int(input())
    tablica.append(y)

# Pobranie wartości x od użytkownika.
x = int(input("Podaj wartość x: "))

# Wyświetlenie wprowadzonej tablicy współczynników.
print("Oto twoja tablica współczynników:", tablica)
# Obliczenie wartości wielomianu dla podanej wartości x przy użyciu metody Hornera.
wynik = horner(tablica, x)
# Wyświetlenie obliczonego wyniku.
print("Wynik wielomianu dla x =", x, "wynosi", wynik)