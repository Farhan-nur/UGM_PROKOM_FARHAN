nilai_mahasiswa = []
while True:
    print("1. Tambahkan data nilai mahasiswa")
    print("2. Tampilkan semua data nilai mahasiswa")
    print("3. Tampilkan data nilai mahasiswa yang memiliki nilai tertinggi")
    print("4. Tampilkan data nilai mahasiswa yang memiliki nilai terendah")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan anda: ")
    if pilihan == '1':
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        nilai_mahasiswa.append((nama, nilai))
        print("Data mahasiswa telah ditambahkan.")
    elif pilihan == '2':
        if not nilai_mahasiswa:
            print("Data masih kosong")
        else:
            for nama, nilai in nilai_mahasiswa:
                print(f"{nama}: {nilai}")
    elif pilihan == '3':
        if not nilai_mahasiswa:
            print("Data masih kosong")
        else:
            max_nilai = max(nilai_mahasiswa, key=lambda x: x[1])
            print(f"Data nilai mahasiswa yang memiliki nilai tertinggi adalah {max_nilai[0]} dengan nilai {max_nilai[1]}")
    elif pilihan == '4':
        if not nilai_mahasiswa:
            print("Data masih kosong")
        else:
            min_nilai = min(nilai_mahasiswa, key=lambda x: x[1])
            print(f"Data nilai mahasiswa yang memiliki nilai terendah adalah {min_nilai[0]} dengan nilai {min_nilai[1]}")
    elif pilihan == '5':
        break
else:
    print("Pilihan tidak valid")
