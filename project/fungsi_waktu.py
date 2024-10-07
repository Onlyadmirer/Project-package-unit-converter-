konversi_waktu = {
    "detik": {"nama": "Detik", "nilai": 1},
    "menit": {"nama": "Menit", "nilai": 60},
    "jam": {"nama": "Jam", "nilai": 3600},
    "hari": {"nama": "Hari", "nilai": 86400}
}

def konversi_waktu_satuan(satuan1: str, satuan2: str, nilai: float):
    try: