def hornerDzielenie(tablica, x, rzad):
    wynik = []
    for i in range(rzad+1):
        # Obliczenie wartości wielomianu dzielonego przez x za pomocą schematu Hornera
        wartosc = tablica[i] + x * (wynik[-1] if wynik else 0)  # Wykorzystanie wartości poprzedniego kroku lub 0
        wynik.append(wartosc)
    return wynik

def wypiszWielomian(tablica):
    wielomian = ""
    stopien = len(tablica) - 2
    for i, wspolczynnik in enumerate(tablica):
        if wspolczynnik != 0 and i != len(tablica) - 1:
            # Tworzenie ciągu znaków reprezentującego wielomian
            if i == 0:
                wielomian += "("
            if stopien - i > 1:
                wielomian += f"{wspolczynnik}x^{stopien - i}"
            elif stopien - i == 1:
                wielomian += f"{wspolczynnik}x"
            else:
                wielomian += f"{wspolczynnik}"
            if i < len(tablica) - 2:
                wielomian += " + "
        elif i == len(tablica) - 1:
            # Dodanie reszty z dzielenia na koniec wielomianu
            if wspolczynnik != 0:
                wielomian += f") reszta = {wspolczynnik}"

    return wielomian

# Pobranie od użytkownika stopnia wielomianu i jego współczynników
rzad = int(input("Proszę podać rząd wielomianu: "))
tablica = []
print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(rzad + 1):
    y = int(input())
    tablica.append(y)

# Pobranie od użytkownika liczby przez którą będzie dzielony wielomian
x = int(input("Proszę podać liczbę przez którą będziemy dzielić: "))

# Wywołanie funkcji obliczającej dzielenie wielomianu przez x
wynik = hornerDzielenie(tablica, x, rzad)

# Wywołanie funkcji wypisującej wielomian wraz z resztą z dzielenia
wielomian = wypiszWielomian(wynik)
print("\nWynik dzielenia wielomianu przez x:", wielomian)