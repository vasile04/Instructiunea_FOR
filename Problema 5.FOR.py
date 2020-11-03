# Utilizand ciclul FOR, elaborati un program care afiseaza suma nr impare de la 1 la n, care se impart la 3 si 5 (n-introdus de la tastatura)
# suma=s
n=int(input('Introdu valoarea lui n:'))
s=0
for i in range (1, n, +2):
    if (i%3==0) and  (i%5==0):
        s+=i
print('Suma nr impare este:', s)