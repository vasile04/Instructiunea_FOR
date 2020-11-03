n = int(input("Dati un numar: "))
s1 = 0
s2 = 0
s5 = 0
s6 = 0
for i in range(1, n):
    s1 += n
    s2 += ((n - 1) * n)
    s5 += (n / (n + 1))
    s6 += (20 + n)
s3 = 1
factorial = 1
for i in range(2, n):
    factorial *= n
    s3 += factorial
s4 = 0
for i in range(1, ((i * 10) + 1)):
    if (n % 10 == 0):
        s4 += (n + 2)

print("s1 =", s1, "  s2 =", s2, "  s3 =", s3, "  s4 =", s4, "  s5 =", s5, "  s6 =", s6)