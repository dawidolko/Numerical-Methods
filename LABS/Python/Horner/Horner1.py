N = int(input("Podaj stopień wielomianu: "))

tab = []
tab.append([])
tab.append([])
tab.append([])

counter = int(0)
while counter!=N+1:
    tab[0].append(int(input("Podaj współczynnik przy x^" + str(N-counter) + ": ")))
    counter += 1

wsp = int(input("Podaj punkt: "))

counter = int(0)
for n in tab[0]:
    if counter==0:
        tab[1].append(n)
        tab[2].append(n)
    else:
        tab[1].append(wsp*tab[2][counter-1])
        tab[2].append(tab[1][counter] + n)
    counter+=1

counter = int(0)
for n in tab[0]:
    if N-counter==0:
        print("(" + str(n) + ")")
    else: 
        print("(" + str(n) + ")x^" + str(N-counter) + " + ", end = "")
    counter += 1

print("Wartosc tego wielomianu w punkcie " + str(wsp) + ": " + str(tab[2][N]))

print("Iloczyn w(x)/(x-(" + str(wsp) + ")):")
counter = int(0)
for n in tab[2]:
    if N-counter==0:
        print(str(n) + "/(x-(" + str(wsp) + "))" )
    else: 
        print("(" + str(n) + ")x^" + str(N-counter-1) + " + ", end = "")
    counter += 1