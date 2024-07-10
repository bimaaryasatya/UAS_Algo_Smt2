import pandas as pd

data = [
    ["mahasiswa 1", 90, 80],
    ["mahasiswa 2", 50, 60],
    ["mahasiswa 3", 65, 70]
]

df = pd.DataFrame(data, columns=["nama", "Algoritma dan Struktur Data 2", "Matematika Numerik"])

print("Rata-rata nilai untuk setiap mata kuliah:")
print(df[["Algoritma dan Struktur Data 2", "Matematika Numerik"]].mean())

print("Rata-rata nilai untuk setiap mahasiswa:")
print(df[["Algoritma dan Struktur Data 2", "Matematika Numerik"]].mean(axis=1))