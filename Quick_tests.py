
print()
# Zewnętrzna pętla - przechodzi przez całą listę tyle razy, ile jest elementów
n=15
for i in range(n):
    print(i)
    # Wewnętrzna pętla - przechodzi przez listę, porównując sąsiednie elementy
    for j in range(n-i-1):
        print(j,i)
