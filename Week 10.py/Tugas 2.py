matriks = [[0, 0, 0], [0, 0, 0]]
for baris in range(2):
    for kolom in range(3):
        matriks[baris][kolom] = int(input(f"Masukkan nilai untuk elemen [{baris}][{kolom}]: "))
print("\nMatriks yang telah diisi:")
for baris in matriks:
    print(" ".join(map(str, baris)))
