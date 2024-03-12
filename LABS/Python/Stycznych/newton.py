from sympy import sympify, diff

prompt = input("Pamietaj oznaczac:\n\t* jako mnozenie\n\t** jako potegowanie\nPodaj wzor funkcji: ")
f = sympify(prompt)
d1 = diff(f, "x", 1)
d2 = diff(f, "x", 2)

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

x = 1

# Choose first approximation
cond_min = d1.subs("x", min) * d2.subs("x", min)
cond_max = d1.subs("x", max) * d2.subs("x", max)
sec_cond_min = f.subs("x", min) * d2.subs("x", min)
sec_cond_max = f.subs("x", max) * d2.subs("x", max)

if cond_min < 0 and cond_max < 0:
    if sec_cond_min > 0:
        x = min
    else:
        x = max
elif cond_max < 0 and cond_min > 0:
    x = max
else:
    x = min

counter = 0

while abs(f.subs("x", x)) > epsilon:
    x = x - f.subs("x", x)/d1.subs("x", x)
    counter += 1

print(f"\nFunkcja f(x) = {f}")
print(f"ma miejsce zerowe w x = {x}")
print(f"znaleziona w {counter} probach")