# Tipe 1
a = int(input('Masukkan berapa jumlah matakuliah\t: '))
nilai_total = 0
for i in range(a):
    nilai_matkul = input(f"Nilai MK {i+1}: ").upper()
    if nilai_matkul=="A":
        nilai_total += 4
    elif nilai_matkul == "B":
        nilai_total += 3
    elif nilai_matkul == "C":
        nilai_total += 2
    elif nilai_matkul == "D":
        nilai_total += 1
hasil = round((nilai_total/2), ndigits=2)
print(f"hasil IPK Lo\t: {hasil}")

# print(f"Nilai MK {a}")
# print("Nilai MK", a)

# Tipe 2
a = int(input('Masukkan berapa jumlah matakuliah\t: '))
nilai_total = 0
i = 1
while a != 0:
    nilai_matkul = input(f"Nilai MK {i}: ").lower()
    if nilai_matkul=="a":
        nilai_total += 4
    elif nilai_matkul == "b":
        nilai_total += 3
    elif nilai_matkul == "c":
        nilai_total += 2
    elif nilai_matkul == "d":
        nilai_total += 1
    a -= 1 #sebagai pengganti break (pembatas supaya variabel a berkurang hingga memenuhi kondisi a == 0)
    i += 1
hasil = round((nilai_total/2), ndigits=2)
print(f"hasil IPK Lo\t: {hasil}")