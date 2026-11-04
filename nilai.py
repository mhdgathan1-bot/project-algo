jumlah = int(input("Jumlah mahasiswa: "))

while jumlah < 5:
    print("jumlah harus 5")
    jumlah = int(input("jumlah mahasiswa (1-5): "))

total = 0

for i in range (1, jumlah + 1):
    nilai = float(input(f"masukkan nilai mahasiswa {i} : "))
    
    total +=nilai 

rata_rata = total/jumlah
print(f"nilai rata-rata: {rata_rata} ")