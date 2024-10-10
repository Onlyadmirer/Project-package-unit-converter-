# Dictionary konversi menyimpan data satuan kecepatan dan faktor konversinya
konversi = {
    "m/s": {"nama": "Meter per detik (m/s)", "nilai": 1},
    "km/h": {"nama": "Kilometer per jam (km/h)", "nilai": 3.6},
    "mph": {"nama": "Mil per jam (mph)", "nilai": 2.23694},
    "knot": {"nama": "Knot", "nilai": 1.94384},
    "mach": {"nama": "Mach", "nilai": 0.002915}
}
# Fungsi kecepatan menerima tiga argumen: satuan1, satuan2, dan nilai
def kecepatan(satuan1: str, satuan2: str, nilai: float):
    try:
        # Menghitung hasil konversi dengan mengalikan nilai awal dengan faktor satuan
         hasil = nilai * konversi[satuan1]["nilai"] / konversi[satuan2]["nilai"]
         return f"{hasil:.2f}"
      
         # Jika satuan yang dimasukkan tidak ditemukan dalam dictionary 'konversi', maka akan terjadi KeyError
    except KeyError:
       # Pesan kesalahan jika input satuan tidak valid
        return "Input tidak valid"

# Contoh penggunaan fungsi kecepatan dengan berbagai satuan dan nilai
# print(kecepatan("km/h", "m/s", 100))  # Mengonversi 100 km/h ke m/s
# print(kecepatan("mph", "km/h", 60))   # Mengonversi 60 mph ke km/h
# print(kecepatan("m/s", "knot", 20))   # Mengonversi 20 m/s ke knot