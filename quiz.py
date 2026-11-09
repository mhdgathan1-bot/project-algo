nama = input("Masukkan nama mashasiswa:")

if nama.lower() == "andi" :
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80 
else:
    print("Nama mahasiswa tidak ada")

print ("target nilai",target)

perulangan = 0
lulus = False

while perulangan < 3 and lulus == False:
    nilai = int(input("Masukkan nilai: "))
    perulangan += 1
    if nilai >= target:
        lulus = True
        print("selamat",nama,"lulus")
        print("jumlah percobaan",perulangan)
    else:
        print("maaf nilai anda belum mencapai target")

    if lulus == False:
        print(nama,"maaf anda belum berhasil")