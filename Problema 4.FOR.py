#  Utilizand ciclul FOR, elaborati un program care afiseaza toate nr impare de la a la b (n-introdus de la tastatura)
a=int(input('Introdu valoarea lui a: '))
b=int(input('Introdu valoarea lui b: '))
for i in range (a, b):
    if i%2!=0:
        print('Nr impare sunt:', i)