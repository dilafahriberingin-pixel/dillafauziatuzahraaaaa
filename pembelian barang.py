print("Rincian Pembelian Alat Lukis")

buku_gambar = 25000 * 3
papan_lukis = 65000 * 1
cat_air = 40000 * 2
pensil_gambar = 15000 * 3
crayon = 35000 * 1

total = buku_gambar + papan_lukis + cat_air + pensil_gambar + crayon

dapat_diskon = total > 100000

print("Total Pembelian: " + str(total))

if dapat_diskon == True:
    diskon = total * 0.25
    total_akhir = total - diskon
    print("Besar Diskon: " + str(diskon))
    print("dapat diskon!")
    print("Total Bayar: " + str(total_akhir))
else:
    print("Tidak Dapat Diskon!")
    print("Total Bayar: " + str(total))
