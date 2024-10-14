angka = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]
total_ganjil = 0
total_genap = 0
for num in angka:
    if num % 2 == 0:
        total_genap += 1
    else:
        total_ganjil += 1
print("Ini adalah angka genap:", end=" ")
for num in angka:
    if num % 2 == 0:
        print(num, end=", ")
print(f"\nJumlah angka genap: {total_genap} angka")
print("Ini adalah angka ganjil:", end=" ")
for num in angka:
    if num % 2 != 0:
        print(num, end=", ")
print(f"\nJumlah angka ganjil: {total_ganjil} angka")
