print("=" * 10 + "kalkulator" + "=" * 10)

print("tambah")
print("kurang")
print("bagi")
print("kali")
print("sisa bagi")
print("pangkat")
print("=" * 30)

operasi = input("masukan operasi (tambah, kurang, bagi, kali, sisa bagi, pangkat) :")
print("anda memilih :", operasi)
print("=" *30)

x = int(input("masukan nilai pertama:"))
y = int(input("masukan nilai kedua:"))

if operasi == "tambah":
    hasil = x + y
elif operasi == "kurang":
    hasil = x - y
elif operasi == "bagi":
    if y != 0:
        hasil = x / y
    else:
        hasil = "Error!!! Pembagian dengan nol tidak diizinkan"
elif operasi == "kali":
    hasil = x * y
elif operasi == "sisa bagi":
    hasil = x % y
elif operasi == "pangkat":    
    hasil = x ** y
else:
    hasil = "Operasi tidak dikenal"
print("=" *30)

print("Hasil:", hasil)
