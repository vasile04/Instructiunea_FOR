# Utilizand ciclul FOR, elaborati un program care afiseaza toate nr pare de la 1 la n (n-introdus de la tastatura)
n=int(input('Introdu valoarea lui n:'))
for i in range (1, n):
    if i%2==0:
        print('Numerele pare sunt:', i)