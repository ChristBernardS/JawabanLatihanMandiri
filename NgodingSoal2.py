# Tipe 1
bawah = int(input('Masukkan batas bawah\t: '))
atas = int(input('Masukkan batas atas\t: '))

# for variable==0 in range(start, stop, step)

# def ganjil(x, y):
def ganjil(bawah, atas):
    if bawah < atas:
        for i in range(bawah, atas):
            if i%2==1:
                print(i, end='')
                if i < atas-1:
                    print(', ', end=' ')
                else:
                    print('.')
    elif bawah > atas:
        for i in range(bawah, atas, -1):
            if i%2==1:
                print(i, end='')
                if i > atas+1:
                    print(', ', end=' ')
                else:
                    print('.')

ganjil(bawah, atas)

# Tipe 2
def ganjil():
    bawah = int(input('Masukkan batas bawah\t: '))
    atas = int(input('Masukkan batas atas\t: '))
    if bawah < atas:
        for i in range(bawah, atas):
            if i%2==1:
                print(i, end='')
                if i < atas-1:
                    print(', ', end=' ')
                else:
                    print('.')
    elif bawah > atas:
        for i in range(bawah, atas, -1):
            if i%2==1:
                print(i, end='')
                if i > atas+1:
                    print(', ', end=' ')
                else:
                    print('.')
ganjil()