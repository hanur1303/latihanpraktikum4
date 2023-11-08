# Minta pengguna untuk memasukkan tiga bilangan 
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

# inisialisasi list untuk menyimpan bilangan-bilangan tersebut
bilangan = [bilangan1, bilangan2, bilangan3]

# mengurutkan bilangan dari yang terkecil ke yang besar
bilangan.sort()

# menampilkan hasil pengurutan 
print("Bilangan-bilangan yang telah diturunkan: ", bilangan)
