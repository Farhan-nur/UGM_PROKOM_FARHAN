angka = [0.0] * 5
for i in range(5):
    angka[i] = float(input(f"Masukkan angka ke-{i+1}: "))
    print("Angka yang telah dimasukkan sejauh ini:", angka[:i+1])
jumlah_total = sum(angka)
pilihan = input("Apakah Anda ingin melihat 'jumlah' atau 'rata-rata'? ")
if pilihan == "jumlah":
    print("Jumlah total dari angka-angka yang dimasukkan adalah:", jumlah_total)
elif pilihan == "rata-rata":
    rata_rata = jumlah_total / 5
    print("Rata-rata dari angka-angka yang dimasukkan adalah:", rata_rata)
else:
    print("Kesalahan: Silakan masukkan 'jumlah' atau 'rata-rata'.")