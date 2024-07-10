import pandas as pd

data = [
    ["mahasiswa 1", 80, 70],
    ["mahasiswa 2", 90, 85],
    ["mahasiswa 3", 75, 80]
]

df = pd.DataFrame(data, columns=["nama", "nilai 1", "nilai 2"])

print("Rata-rata nilai untuk setiap mata kuliah:")
print(df[["nilai 1", "nilai 2"]].mean())

print("Rata-rata nilai untuk setiap mahasiswa:")
print(df[["nilai 1", "nilai 2"]].mean(axis=1))