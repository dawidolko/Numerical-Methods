from sympy import sympify

prompt = input("Pamietaj oznaczac:\n\t* jako mnozenie\n\t** jako potegowanie\nPodaj wzor funkcji: ")
f = sympify(prompt)

a = float(input("Podaj poczatek przedzialu: "))
b = float(input("Podaj koniec przedzialu: "))
min = min(a, b)
max = max(a, b)

# Bolzano-Cauchy theorem
if f.subs("x", min) * f.subs("x", max) > 0:
    print("\nTwierdzenie Bolzano-Cauchy'ego nie jest spelnione")
    print(f"W przedziale [{min}, {max}] najpewniej nie ma miejsca zerowego")
    exit(1)

epsilon = float(input("Wybierz dokladnosc(epsilon): "))

temp_min = min
temp_max = max
x = (temp_min+temp_max)/2
counter = 1
while abs(f.subs("x", x)) > epsilon:
    x = (temp_min+temp_max)/2

    counter += 1

    if f.subs("x", x) * f.subs("x", temp_min) <= 0:
        temp_max = x
    else:
        temp_min = x

print(f"\nFunkcja f(x) = {f}")
print(f"ma miejsce zerowe w x = {x}")
print(f"znaleziona w {counter} probach")