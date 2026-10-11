n = 5
def silnia_rekurencyjna(n):
    if n == 1 or n == 0:
        return 1
    else: return n * silnia_rekurencyjna(n-1)
print (silnia_rekurencyjna(n))