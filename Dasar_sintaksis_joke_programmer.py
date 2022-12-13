"""
Semua Sintaksis dasar bahasa pemrograman terdiri dari:
1. Sequential   : Langkah Berurutan
2. Percabangan  : Langkah melompat jika kondisi terpenuhi
3. Pengulangan  : Mengulangi langkah yang sama hingga kondisi terpenuhi
"""
# Sequential
print('Ibu berkata, "Pergi ke Toko"')
print('Budi mejawab,"Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 Susu, jika ada telur beli 6"')
print("Maka Budi pergi ke Toko")
print('Maka Budi pergi ke Toko')

#Percabangan
jumlah_susu = 173
jumlah_telur = 1587
print(f"Jumlah Botol susu {jumlah_susu} btl")
print(f"Jumlah Telur {jumlah_telur} butir")
if jumlah_susu > 0:
    print("Budi mengecek harganya, dan ternyata uang cukup")
    if jumlah_telur == 0:
        print("budi membeli 1 botol susu")
    else:
        print("budi membeli 6 telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")