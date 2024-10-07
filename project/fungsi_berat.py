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
def berat(satuan1:str, satuan2:str, nilai:float):
    try:
        hasil = nilai * konversi[satuan1]["nilai"] / konversi[satuan2]["nilai"]
        return f"{hasil:.2f} "
    except KeyError:
        print("input tidak valid")