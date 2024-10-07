konversi = {
    "m/s": {"nama": "Meter per detik (m/s)", "nilai": 1},
    "km/h": {"nama": "Kilometer per jam (km/h)", "nilai": 3.6},
    "mph": {"nama": "Mil per jam (mph)", "nilai": 2.23694},
    "knot": {"nama": "Knot", "nilai": 1.94384},
    "mach": {"nama": "Mach", "nilai": 0.002915}
}

def kecepatan(satuan1: str, satuan2: str, nilai: float):
    try:

        