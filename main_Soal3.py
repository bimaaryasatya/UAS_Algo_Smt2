import Soal3 as s3

antrian = s3.AntrianRestoran()

while True:
    print("\n1. Tambahkan pesanan")
    print("2. Layani pesanan")
    print("3. Tampilkan antrian")
    print("4. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        pesanan = input("Masukkan pesanan: ")
        antrian.enqueue(pesanan)
    elif pilihan == "2":
        antrian.dequeue()
    elif pilihan == "3":
        antrian.tampilkan_antrian()
    elif pilihan == "4":
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")