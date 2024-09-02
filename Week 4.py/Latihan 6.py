guweh = input("Pilih (batu, gunting, kertas): ")
lawan = "gunting"
if guweh == lawan:
    hasil = "Seri!"
elif guweh == "batu":
    if lawan == "gunting":
        hasil = "Guweh menang!"
    else:
        hasil = "Guweh kalah!"
elif guweh == "gunting":
    if lawan == "kertas":
        hasil = "Guweh menang!"
    else:
        hasil = "Guweh kalah!"
elif guweh == "kertas":
    if lawan == "batu":
        hasil = "Guweh menang!"
    else:
        hasil = "Guweh kalah!"
else:
    hasil = "Pilihan tidak valid"
print(f"Guweh memilih: {guweh}")
print(f"Lawan memilih: {lawan}")
print(hasil)
