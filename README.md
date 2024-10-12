# Project_8

=======================================

# Konversi Satuan Berat

=======================================

Untuk mengkonversi berat, Anda dapat menggunakan fungsi 'berat' dari modul 'fraier'.
Berikut adalah contoh cara penggunaannya: 1. Import modul 'vertopy'

          ```python
             import vertopy
          ```

       2. Tentukan nilai berat yang ingin dikonversi,
          serta satuan asli dan satuan yang akan dikonversi.
          Contoh:

          ```python
             from_unit = "g"  # satuan asli (gram)
             to_unit = "kg"  # satuan yang akan dikonversi (kilogram)
             nilai = 50  # nilai berat dalam gram yang akan dikonversi ke kilogram


             CATATAN:
             from_unit harus diisi string
             to_unit harus diisi string
             nilai harus diisi float/integer
          ```

       3. Panggil fungsi 'berat' dengan parameter 'from_unit', 'to_unit', dan 'nilai':


          ```python
             hasil = vertopy.berat(from_unit, to_unit, nilai)
          ```

       4. Contoh lengkap:

          ```python
             import vertopy

             hasil = vertopy.berat("g", "kg", 50)
             print(hasil)

             Output:
             0.05 #jadi, 50 gram dikonversi ke kilogram adalah 0.05 kilogram
          ```
          ```

=======================================

# Konversi Satuan Berat

=======================================

Project ini adalah sebuah program sederhana untuk mengkonversi satuan kecepatan antara beberapa unit yang umum digunakan seperti
meter per detik (m/s),
kilometer per jam (km/h),
mil per jam (mph), knot, dan mach.

Program ini ditulis dalam bahasa Python menggunakan dictionary untuk menyimpan faktor konversi dari setiap satuan kecepatan.

## Cara Kerja

- Program menyimpan satuan-satuan kecepatan dan faktor konversinya di dalam sebuah dictionary bernama `konversi`.
- Fungsi `kecepatan(satuan1, satuan2, nilai)` menerima tiga argumen:

  - `satuan1`: Satuan kecepatan awal (misal: "km/h", "mph").
  - `satuan2`: Satuan kecepatan yang akan dikonversikan (misal: "m/s", "knot").
  - `nilai`: Nilai kecepatan yang akan dikonversikan (misal: 100, 60).

- Fungsi ini kemudian menghitung hasil konversi dengan mengalikan nilai awal dengan faktor satuan pertama (`satuan1`) dan membaginya dengan faktor satuan kedua (`satuan2`).
- Jika satuan yang dimasukkan tidak valid atau tidak terdapat di dalam dictionary, fungsi akan mengembalikan pesan "Input tidak valid".

## Contoh Penggunaan

Berikut adalah contoh penggunaan dari fungsi `kecepatan()`:

```python
# Mengonversi 100 km/h ke m/s
print(kecepatan("km/h", "m/s", 100))  # Output: 27.78

# Mengonversi 60 mph ke km/h
print(kecepatan("mph", "km/h", 60))  # Output: 96.56

# Mengonversi 20 m/s ke knot
print(kecepatan("m/s", "knot", 20))  # Output: 38.88


Struktur Program :
- konversi: Dictionary yang menyimpan satuan kecepatan dan faktor konversinya.
- kecepatan(satuan1, satuan2, nilai): Fungsi untuk mengonversi nilai kecepatan dari satu satuan ke satuan lainnya.
- try-except: Digunakan untuk menangani error jika satuan yang dimasukkan tidak valid.

Satuan yang Didukung :
- m/s  : Meter per detik
- km/h : Kilometer per jam
- mph  : Mil per jam
- knot : Knot (mil laut per jam)
- mach : Mach (kecepatan suara di udara)

Error Handling :
Jika satuan yang dimasukkan tidak ditemukan dalam dictionary konversi, fungsi akan mengembalikan pesan "Input tidak valid". Hal ini ditangani menggunakan blok try-except.

Lisensi :
Proyek ini bersifat open-source dan dapat digunakan atau dimodifikasi sesuai kebutuhan.
File `README.md` ini menjelaskan cara kerja kode, penggunaan, serta satuan-satuan yang didukung. Anda bisa menyesuaikan lebih lanjut sesuai kebutuhan proyek Anda.
```

=======================================

# Konversi Satuan Panjang

=======================================

Aplikasi ini digunakan untuk mengkonversi satuan panjang dari satu satuan ke satuan lainnya. Aplikasi ini menggunakan fungsi panjang yang dapat mengkonversi satuan panjang dengan menggunakan tabel konversi yang telah ditentukan.

## Cara Penggunaan

Untuk menggunakan aplikasi ini, Anda perlu memanggil fungsi panjang dengan tiga argumen:

### 1. dari_satuan: satuan panjang awal yang ingin dikonversi

### 2. ke_satuan : satuan panjang yang ingin dikonversi ke

### 3. nilai : nilai yang ingin dikonversi

## Contoh:

### print(panjang("km", "m", 5)) # Output: 5000.00

Pada contoh di atas, fungsi panjang akan mengkonversi 5 kilometer menjadi meter.

Satuan yang Didukung
Aplikasi ini mendukung konversi antara satuan-satuan berikut:

- **m (kilometer)**
- **hm (hektometer)**
- **dam (dekameter)**
- **m (meter)**
- **dm (desimeter)**
- **cm (centimeter)**
- **mm (milimeter)**

## Error Handling

Jika satuan yang dimasukkan tidak ditemukan, package akan mengembalikan pesan error "Satuan tidak ditemukan".

## License

Package ini dibuat dengan lisensi MIT. Anda bebas menggunakan dan memodifikasi aplikasi ini untuk keperluan Anda.

=======================================

# Konversi Satuan Suhu

=======================================

Untuk mengkonversi suhu, Anda dapat menggunakan fungsi 'suhu' dari modul 'vertopy'.
Berikut adalah contoh cara penggunaannya: 1. Import modul 'vertopy'

          ```python
             import vertopy
          ```

       2. Tentukan nilai suhu yang ingin dikonversi,
          serta satuan awal dan satuan yang akan dikonversi.
          Contoh:

          ```python
             satuan1 = "c"  # satuan asli (celcius)
             satuan2 = "k"  # satuan yang akan dikonversi (kelvin)
             nilai = 50  # nilai suhu dalam celcius yang akan dikonversi ke kelvin


             CATATAN:
             satuan1 harus diisi string
             satuan2 harus diisi string
             nilai harus diisi float/integer
          ```

       3. Panggil fungsi 'suhu' dengan parameter 'satuan1', 'satuan2', dan 'nilai':

          ```python
             hasil = vertopy.suhu(satuan, satuan2, nilai)
          ```

       4. Contoh lengkap:

          ```python
             import vertopy

             import vertopy
             print(vertopy.suhu('c', 'k', 50))

             Output:
             323.15 #jadi, 50 celcius dikonversi ke kelvin adalah 323.15 kelvin
          ```

========================================

# Konversi Waktu Berdasarkan Detik

========================================

## Deskripsi

Program ini adalah kamus konversi waktu yang dapat mengubah nilai dari satu satuan waktu ke satuan waktu lainnya, seperti detik, menit, jam, atau hari. Dengan menggunakan kamus yang telah didefinisikan, program dapat menghitung hasil konversi antar satuan waktu berdasarkan nilai konversi yang telah ditetapkan.

## Kamus Waktu

Program ini menggunakan kamus (`konversi_waktu`) yang menyimpan satuan waktu dan nilai konversinya dari detik. Berikut adalah satuan waktu yang didukung:

- **Detik**: 1 detik = 1 detik
- **Menit**: 1 menit = 60 detik
- **Jam**: 1 jam = 3600 detik
- **Hari**: 1 hari = 86400 detik

## Fungsi Utama

### `konversi_waktu_satuan(satuan1: str, satuan2: str, nilai: float) -> str`

Fungsi ini digunakan untuk mengonversi nilai dari satu satuan waktu ke satuan waktu lainnya.

#### Parameter:

- **satuan1**: Satuan waktu awal (contoh: 'detik', 'menit', 'jam', 'hari')
- **satuan2**: Satuan waktu target (contoh: 'detik', 'menit', 'jam', 'hari')
- **nilai**: Nilai yang ingin dikonversi

#### Return:

- Hasil konversi dalam bentuk string dengan format angka hingga dua desimal, atau pesan kesalahan jika input tidak valid.

#### Contoh Penggunaan:

```python
print(konversi_waktu_satuan('detik', 'menit', 120))  # Output: "2.00"
print(konversi_waktu_satuan('hari', 'jam', 1))       # Output: "24.00"
```

## Penanganan Error

Jika pengguna memasukkan satuan waktu yang tidak dikenali (selain dari 'detik', 'menit', 'jam', atau 'hari'), fungsi akan mengembalikan pesan kesalahan `"Input tidak valid"`.

## Cara Penggunaan

1. Pastikan Anda sudah mendefinisikan kamus `konversi_waktu` seperti di contoh.
2. Panggil fungsi `konversi_waktu_satuan` dengan parameter yang sesuai.
3. Fungsi akan mengembalikan hasil konversi dalam bentuk string yang diformat hingga dua angka di belakang koma.

## Lisensi

Proyek ini bersifat open-source dan dapat digunakan oleh siapa saja tanpa batasan.
