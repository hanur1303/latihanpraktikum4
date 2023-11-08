import random

# meminta pengguna untuk memasukkan nilai n
n = int(input("masukkan nilai n:"))

# inisialisasi penghitung 
count = 0 
while count < n:
    random_number = random.random() # menghasilkan bilangan acak antara 0 dan 1
    if random_number < 0.5:
        print(random_number)
        count += 1

print("selesai")