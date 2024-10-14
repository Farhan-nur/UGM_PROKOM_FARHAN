n = int(input("Masukkan jumlah elemen dalam array: "))
nilai_mahasiswa = []
for i in range(1, n + 1):
    nilai_mahasiswa.append(i)
print(f"Data Array: {nilai_mahasiswa}")
kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))
kelipatan_elements = []
for elemen in nilai_mahasiswa:
    if elemen % kelipatan == 0:
        kelipatan_elements.append(elemen)
if kelipatan_elements:
    print(f"Elemen yang merupakan kelipatan dari {kelipatan}: {kelipatan_elements}")
else:
    print("Tidak ada elemen yang merupakan kelipatan dari bilangan tersebut.")
