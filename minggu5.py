# Soal 1
def perkalian(x, y):
    p = x * y
    return p

a = int(input('Masukkan angka\t: '))
b = int(input('Masukkan angka\t: '))
print(f"{a} x {b} = ", end='')
for i in range(a-1):
    print(b, end=' ')
    for j in range(1):
        print('+', end=' ')
print(b, end=' ')
print(f"= {perkalian(a, b)}")

# Soal 2
a = int(input('bawah\t= '))
b = int(input('atas\t= '))
if a < b:
    for i in range(a, b):
        if i%2==1:
            print(i, end=', ')
elif a > b:
    for i in range(b, a, -1):
        if i%2==1:
            print(i, end=', ')
else:
    None

# Soal 3
a = int(input('Jumlah mata kuliah\t: '))
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(a):
    b = input(f"Nilai MK {i+1}: ")
    c[i] = b
d = 0
for j in range(len(c)):
    if c[j] == 'A':
        d += 4
    elif c[j] == 'B':
        d += 3
    elif c[j] == 'C':
        d += 2
    elif c[j] == 'D':
        d += 1
print(round(d/a, ndigits=2))