import sympy as sp
import matplotlib.pyplot as plt
from collections import Counter
import re


# Instrukcja dla użytkownika
def print_instructions():
    print("""
Wprowadź wyrażenie matematyczne, które chcesz obliczyć. Oto przykłady:
- Aby obliczyć pierwiastek: sqrt(x)
- Aby użyć funkcji trygonometrycznych: sin(x), cos(x)
- Aby obliczyć całkę: integrate(sqrt(1+x), (x, 0, 1))
- Aby zakończyć, wpisz 'exit'
""")


# Definicja funkcji do przetwarzania wyrażeń matematycznych i ich obliczania
def calculate_expression(expression):
    x = sp.symbols('x')
    try:
        # Przetwarzanie i obliczanie wyrażenia
        result = sp.sympify(expression).evalf()
    except Exception as e:
        print("Wystąpił błąd przy przetwarzaniu wyrażenia: ", str(e))
        return None
    return result


# Funkcja do zbierania i analizowania operacji matematycznych
def analyze_operations(expression):
    operations = {
        '*': 'mnożenie',
        '**': 'potęgowanie',
        'sqrt': 'pierwiastkowanie',
        'sin': 'funkcja sinus',
        'cos': 'funkcja cosinus',
        'integrate': 'całkowanie',
        # Dodaj więcej operacji matematycznych według potrzeb
    }

    op_counter = Counter()
    for op, name in operations.items():
        if re.search(re.escape(op), expression):
            op_counter[name] += 1
    return op_counter


# Interakcja z użytkownikiem i główna pętla programu
def main():
    history = Counter()
    print_instructions()

    while True:
        expression = input("Wprowadź wyrażenie: ")
        if expression.lower() == 'exit':
            break

        result = calculate_expression(expression)
        if result is not None:
            print("Wynik wyrażenia:", result)
            # Analiza i aktualizacja historii operacji
            operations_used = analyze_operations(expression)
            history.update(operations_used)

    # Generowanie histogramu
    if history:
        plt.bar(history.keys(), history.values())
        plt.xlabel('Operacje')
        plt.ylabel('Liczba użycia')
        plt.title('Histogram użycia operacji matematycznych')
        plt.show()


if __name__ == '__main__':
    main()
