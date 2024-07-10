mahasiswa = []

while True:
    print("Menu:")
    print("1. Tambahkan data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nim = int(input("Masukkan NIM mahasiswa: "))
        mahasiswa.append({"nama": nama, "nim": nim})
        print("Data mahasiswa berhasil ditambahkan")

    elif pilihan == "2":
        if len(mahasiswa) == 0:
            print("Tidak ada data mahasiswa tersedia.")
        else:
            print("Data Mahasiswa:")
            for i, data in enumerate(mahasiswa, 1):
                print(f"{i}. {data['nama']} - {data['nim']}")

    elif pilihan == "3":
        print("Keluar")
        break

    else:
        print("Pilihan Tidak Valid tidak valid")