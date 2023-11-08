# inisialisasi variabel untuk menyimpan bilangan terbesar
max_number = None

while True:
    input_number = int(input("masukkan angka (0 untuk berhenti): "))

    # cek apakah pengguna memasukkan 0
    if input_number == 0:
        break
    #periksa apakah bilangan saat ini lebih besar dari yang sebelumnya
    if max_number is None or input_number > max_number:
        max_number = input_number

if max_number is not None:
    print("Bilangan terbesar adalah:", max_number)
else:
    print("Tidak Ada bilangan yang dimasukkan.")