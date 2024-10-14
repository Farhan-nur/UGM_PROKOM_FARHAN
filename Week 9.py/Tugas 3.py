bilangan = [4, 5, 11, 12, 14, 16, 16, 19]
bilangan_prima = []
jumlah_bilangan_prima = 0
for nilai in bilangan:
    if nilai > 1: 
        adalah_prima = True 
        for i in range(2, int(nilai**0.5) + 1):
            if nilai % i == 0:
                adalah_prima = False
                break
        if adalah_prima:
            bilangan_prima.append(nilai)  
            jumlah_bilangan_prima += 1  
print("Bilangan prima yang ditemukan:", bilangan_prima)
print("Total bilangan prima:", jumlah_bilangan_prima)
