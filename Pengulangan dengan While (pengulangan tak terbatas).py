"""
Program Pengulangan Membaca buku dengan While sampai paham
"""

jumlah_buku = 10
print('Ibu berkata,"Baca semua buku"')
Jumlah_baca = 0

Jumlah_dipahami = 0
print(f'Jumlah buku yang sudah dibaca {Jumlah_dipahami}')

while Jumlah_baca < jumlah_buku * 2:
    Jumlah_baca = Jumlah_baca + 1
    if Jumlah_dipahami == 9:
        print(f"Buku ke {Jumlah_dipahami + 1} belum paham")
    else:
        Jumlah_dipahami = Jumlah_dipahami + 1
        print(f"Buku ke {Jumlah_dipahami} sudah dibaca dan dipahami")

print(f"jumlah buku yang sudah dibaca {Jumlah_dipahami}")
if Jumlah_dipahami == jumlah_buku:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print(f'Bu, tidak semua buku bisa dipahami". '
          f'Budi hanya bisa memahami {Jumlah_dipahami} buku')
