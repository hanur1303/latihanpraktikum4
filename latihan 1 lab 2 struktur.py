# Minta Pengguna untuk masukkan dua bilangan 
bilangan1 =int(input("masukkan bilangan pertama: "))
bilangan2 = int(input("masukkan bilangan kedua: "))

#inisialisasi variabel untuk bilangan terbesar
bilangan_terbesar = bilangan1

# periksa apakah bilangan kedua lebih besar dari bilangan_terbesar
if bilangan2 > bilangan_terbesar:
    bilangan_terbesar = bilangan2

# tampilkan bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar)    