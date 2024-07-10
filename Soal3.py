# antrian_restoran.py

class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        """Tambahkan pesanan baru ke dalam antrian"""
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' ditambahkan ke dalam antrian.")

    def dequeue(self):
        """Hapus antrian dari depan"""
        if not self.antrian:
            print("Antrian kosong.")
            return None
        pesanan = self.antrian.pop(0)
        print(f"Pesanan '{pesanan}' dilayani.")
        return pesanan

    def tampilkan_antrian(self):
        """Tampilkan antrian saat ini"""
        print("Antrian saat ini:")
        for i, pesanan in enumerate(self.antrian):
            print(f"{i+1}. {pesanan}")

