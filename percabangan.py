# # # input
# nilai = int(input("masukkan nilai: "))
# # proses
# if nilai >=80 and nilai<=100:
#     print("Anda mendapatkan nilai A")
# elif nilai>=70 and nilai<=80:
#     print("Anda mendapatkan nilai B")
# elif nilai>=50 and nilai<=70:
#     print("Anda mendapatkan nilai C")
# elif nilai>=30 and nilai<=50:
#     print("Anda mendapatkan nilai D")
# elif nilai>=0 and nilai<=20:
#     print("Anda mendapatkan nilai E")
# else:
#     print("DATA TIDAK VALID")

print("======LATIHAN======")
barang = input("masukkan Nama Barang :")
#input
if barang == "kulkas":
    harga = 2000
    diskon = 0.10 * harga
    total = harga - diskon 
    print("barang: kulkas")
    print("harga asli:", harga)
    print("diskon: 10%")
    print("harga setelah diskon:", int(total))
elif barang =="TV":

    harga = 3500
    diskon = 0.05 * harga
    total = harga - diskon 
    print("barang: tv")
    print("harga asli:", harga)
    print("diskon: 5%")
    print("harga setelah diskon:", int(total))
elif barang =="radio":
    harga = 1500
    total = harga
    print("barang: radio")
    print("harga asli:", harga)
    print("diskon tidak ada")
    print("harga total:",harga)
else:
    print("barang tidak tersedia")
