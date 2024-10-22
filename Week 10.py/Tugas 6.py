Array1 = [
    [4, 6],
    [1, 7]
]

Array2 = [
    [2, 3],
    [5, 6]
]
HasilJumlah = [
    [0, 0],
    [0, 0]
]
for i in range(len(Array1)):
    for j in range(len(Array1[0])):
        HasilJumlah[i][j] = Array1[i][j] + Array2[i][j]
print("Hasil Penjumlahan Array1 dan Array2:")
for baris in HasilJumlah:
    print(baris)
