# Pobieranie stopnia wielomianu od użytkownika
N = int(input("Podaj stopień wielomianu: "))

# Inicjalizacja listy na współczynniki wielomianu, pomocnicze obliczenia i wyniki
tab = [[], [], []]

# Wczytywanie współczynników wielomianu od użytkownika
counter = 0
while counter != N + 1:
    tab[0].append(int(input("Podaj współczynnik przy x^" + str(N - counter) + ": ")))
    counter += 1

# Pobieranie punktu, w którym ma być obliczona wartość wielomianu
wsp = int(input("Podaj punkt: "))

# Obliczanie wartości wielomianu w podanym punkcie
counter = 0
for n in tab[0]:
    if counter == 0:
        tab[1].append(n)
        tab[2].append(n)
    else:
        tab[1].append(wsp * tab[2][counter - 1])
        tab[2].append(tab[1][counter] + n)
    counter += 1

# Wyświetlanie postaci wielomianu
counter = 0
for n in tab[0]:
    if N - counter == 0:
        print("(" + str(n) + ")")
    else:
        print("(" + str(n) + ")x^" + str(N - counter) + " + ", end="")
    counter += 1

# Wyświetlanie wartości wielomianu w podanym punkcie
print("Wartość tego wielomianu w punkcie " + str(wsp) + ": " + str(tab[2][N]))

# Wyświetlanie postaci ilorazu wielomianu przez (x - wsp)
print("Iloczyn w(x)/(x-(" + str(wsp) + ")):")
counter = 0
for n in tab[2]:
    if N - counter == 0:
        print(str(n) + "/(x-(" + str(wsp) + "))")
    else:
        print("(" + str(n) + ")x^" + str(N - counter - 1) + " + ", end="")
    counter += 1
