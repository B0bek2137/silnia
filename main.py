def silnia_iteracyjna(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik
print (silnia_iteracyjna(6))