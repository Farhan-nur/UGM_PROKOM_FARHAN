siswa_data = []
for index in range(5):
    nama_siswa = input("Masukkan nama siswa: ")
    nilai_siswa = int(input("Masukkan nilai siswa: "))
    if nilai_siswa >= 70:
        kelulusan = "Lulus"
    else:
        kelulusan = "Tidak Lulus"
    siswa_data.append((nama_siswa, nilai_siswa, kelulusan))
print("\nDaftar Kelulusan Siswa:")
for data in siswa_data:
    print(f"Nama: {data[0]}, Nilai: {data[1]}, Status: {data[2]}")
