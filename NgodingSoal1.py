# Tipe 1
def perkalian(x, y):
    z = x * y
    return z

a = int(input('Masukkan angka\t: '))
b = int(input('Masukkan angka\t: '))
print(a, 'x', b, '=', end=' ')
for i in range(a - 1):
    print(b, end=' ')
    print('+', end=' ')
print(b, end=' ')
print('=', perkalian(a, b))

def perkalian():
    a = int(input('Masukkan angka\t: '))
    b = int(input('Masukkan angka\t: '))
    print(a, 'x', b, '=', end=' ')
    for i in range(a - 1):
        print(b, end=' ')
        print('+', end=' ')
    print(b, end=' ')
    print('=', a*b)

perkalian()

# Tipe 2
a = int(input('Masukkan angka\t: '))
b = int(input('Masukkan angka\t: '))

def perkalian(x, y):
    z = x * y
    return z
i = 1 
print(a, 'x', b, '=', end=' ')
for i in range(a):
    print(b, end=' ')
    if i < a-1:
        print('+', end=' ')
    else:
        print('=', end=' ')

print(perkalian(a, b))

# Tipe 3
a = int(input('Masukkan angka\t: '))
b = int(input('Masukkan angka\t: '))

def perkalian(x, y):
    z = x * y
    return z

c = 0
print(a, 'x', b, '=', end=' ')
while True:
    print(b, end=' ')
    if c < a-1:
        print('+', end=' ')
        c += 1
    else:
        print('=', end=' ')
        break

print(perkalian(a, b))