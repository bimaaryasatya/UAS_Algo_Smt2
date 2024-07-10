class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def display_info(self):
        return f'Nama: {self.nama}\nWarna: {self.warna}\nRasa: {self.rasa}'

class VitaminBuah(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def display_vitamin_info(self):
        self.display_info()
        print(f"{self.display_info()}\nVitamin: {self.vitamin}\n{self.display_info}")

vb = VitaminBuah("Apel", "Merah", "Manis", "Vitamin C")
vb.display_vitamin_info()
