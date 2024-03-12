def hornerDzielenie(tablica, x, rzad):
    wynik = []
    for i in range(rzad):
        wartosc = tablica[i] + x * (wynik[-1] if wynik else 0)
        wynik.append(wartosc)
    return wynik

def wypiszWielomian(tablica):
    wielomian = ""
    stopien = len(tablica) - 1
    for i, wspolczynnik in enumerate(tablica):
        if wspolczynnik != 0 & wspolczynnik != len(tablica)-1:
            if i == 0:
                wielomian+="("
            if stopien - i > 1:
                wielomian += f"{wspolczynnik}x^{stopien-i}"
            elif stopien - i == 1:
                wielomian += f"{wspolczynnik}x"
            else:
                wielomian += f"{wspolczynnik}"
            if i < len(tablica) - 1:
                wielomian += " + "

    wielomian +=")\t(x - "+f"{tablica[len(tablica)-1]})"
    return wielomian

rzad = int(input("Proszę podać rząd wielomianu: "))
tablica = []
print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(rzad + 1):
    y = int(input())
    tablica.append(y)

x = int(input("Proszę podać liczbę przez, którą będziemy dzielić: "))

wynik = hornerDzielenie(tablica, x, rzad)
wielomian = wypiszWielomian(wynik)
print("\nWynik dzielenia wielomianu przez x:", wielomian)