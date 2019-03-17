import math

m = int(input())
n = int(input())
x = int(input())
tablica = {}


for i in range(m, n + 1):
    tablica[i] = (i**2, i**3, round(math.sqrt(i), 5));

if x >= m and x <= n:
    print(tablica[x])
else:
    print("nema podatoci")    

print (sorted(tablica.items()))    