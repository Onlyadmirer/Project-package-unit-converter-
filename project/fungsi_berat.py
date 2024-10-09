# Definisikan kamus konversi satuan berat
# Kamus ini berisi pasangan key-value, di mana key adalah singkatan satuan berat
# dan value adalah dictionary yang berisi nama satuan berat dan nilai konversinya
konversi = {
    "mg": {"nama": "Miligram(mg)", "nilai": 1},
    "cg": {"nama": "Centigram( cg)", "nilai": 10},
    "dg": {"nama": "Desigram(dg)", "nilai": 100},
    "g":  {"nama": "Gram(g)", "nilai": 1000},
    "dag":{"nama": "Dekagram(dag)", "nilai": 10000},
    "hg": {"nama": "Hektogram(hg)", "nilai": 100000},
    "kg": {"nama": "Kilogram(kg)", "nilai": 1000000},
    "ton":{"nama": "Ton", "nilai": 1000000000}
}
# Fungsi untuk mengkonversi satuan berat
def berat(satuan1:str, satuan2:str, nilai:float):
    try:
        # Membuat variable hasil 
        # untuk menghitung hasil konversi dengan mengalikan nilai awal dengan nilai satuan1 kemudian dibagi dengan nilai satuan 2
        hasil = nilai * konversi[satuan1]["nilai"] / konversi[satuan2]["nilai"]
        return f"{hasil:.2f}"
    except KeyError:
        # Jika input tidak valid, cetak pesan kesalahan
        print("input tidak valid")
