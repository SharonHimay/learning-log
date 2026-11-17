# Latihan soal

Kumpulan soal latihan beserta tautan ke kode jawabannya.

- [Python](#python)
- [C](#c)
- [Linux](#linux)

---

## Python

### Sesi 1

#### Perkenalan · Latihan 1 (pemanasan)

Buat program yang meminta namamu dan jurusanmu, lalu menampilkan kalimat seperti:
`Halo, nama saya Sharon dan saya kuliah di Teknik Telekomunikasi.`

Jawaban: [`Perkenalan.py`](python/Sesi%201/Perkenalan.py)

#### Celcius ke Farenheit · Latihan 2

Buat program konversi suhu Celsius ke Fahrenheit. Program meminta suhu dalam Celsius, lalu menampilkan hasilnya. Rumusnya: `F = C * 9/5 + 32`.

Jawaban: [`Celcius ke Farenheit.py`](python/Sesi%201/Celcius%20ke%20Farenheit.py)

#### dBm ke  Mw · Latihan 3 (versi telekom)

Daya sinyal sering ditulis dalam dBm. Buat program yang meminta nilai dBm, lalu menampilkan dayanya dalam miliwatt (mW). Rumusnya: `P(mW) = 10 ** (dBm / 10)`

Jawaban: [`dBm ke  Mw.py`](python/Sesi%201/dBm%20ke%20%20Mw.py)

### Sesi 2

#### Genap atau ganjil · Latihan 1 (pemanasan)

Program meminta sebuah bilangan bulat, lalu menampilkan "Genap" atau "Ganjil". Petunjuk: pakai operator sisa bagi `%` yang dipelajari di Sesi 1.

Jawaban: [`Genap atau ganjil.py`](python/Sesi%202/Genap%20atau%20ganjil.py)

#### Grade nilai · Latihan 2

Program meminta nilai ujian (0-100) lalu menampilkan grade A/B/C/D memakai `elif`, dengan batas seperti contoh di materi. Tambahan: kalau nilai di luar 0-100, tampilkan "Nilai tidak valid".

Jawaban: [`Grade nilai.py`](python/Sesi%202/Grade%20nilai.py)

#### Alarm suhu ruang server · Latihan 3 (versi AIoT)

Buat program "alarm suhu ruang server". Program meminta suhu (C) dan kelembapan (%), lalu:

- Suhu lebih dari 35 atau kelembapan lebih dari 80 → tampilkan `BAHAYA`
- Suhu antara 28 dan 35 (inklusif) → tampilkan `WASPADA`
- Selain itu → tampilkan `AMAN`

Tes dengan pasangan ini:

| Suhu | Kelembapan | Seharusnya |
|---|---|---|
| 25 | 50 | AMAN |
| 30 | 50 | WASPADA |
| 40 | 50 | BAHAYA |
| 25 | 90 | BAHAYA |

Jawaban: [`Alarm suhu ruang server.py`](python/Sesi%202/Alarm%20suhu%20ruang%20server.py)

### Sesi 3

#### Angka 1-10 dan totalnya · Latihan 1 (pemanasan)

Tampilkan angka 1 sampai 10, lalu di akhir tampilkan jumlah totalnya. Hasil totalnya harus 55.

Jawaban: [`Angka 1-10 dan totalnya.py`](python/Sesi%203/Angka%201-10%20dan%20totalnya.py)

#### Tabel perkalian · Latihan 2

Program meminta sebuah bilangan bulat `n`, lalu menampilkan tabel perkalian `n` dari 1 sampai 10. Contoh kalau n = 3:

```
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
```

Jawaban: [`Tabel perkalian.py`](python/Sesi%203/Tabel%20perkalian.py)

#### Validasi input sensor suhu · Latihan 3 (versi AIoT)

Buat program validasi input sensor suhu. Program terus meminta suhu (C) sampai pengguna memasukkan nilai yang masuk akal, yaitu antara -10 dan 80 (inklusif). Kalau di luar rentang itu, tampilkan `Pembacaan sensor tidak valid, ulangi.` dan minta lagi. Setelah valid, tampilkan `Suhu diterima: ...`.

Tes dengan urutan input: 200, -50, 25. Dua input pertama harus ditolak, dan input ketiga diterima. Petunjuk: pakai `while True` dan `break`.

Jawaban: [`Validasi input sensor suhu.py`](python/Sesi%203/Validasi%20input%20sensor%20suhu.py)

#### Rata-rata 5 pembacaan · Tantangan (opsional)

Minta 5 pembacaan suhu dengan `for`, jumlahkan dengan pola akumulator, lalu tampilkan rata-ratanya. Coba dengan 20, 22, 24, 26, 28; rata-ratanya harus 24.0.

Jawaban: [`Rata-rata 5 pembacaan.py`](python/Sesi%203/Rata-rata%205%20pembacaan.py)

### Sesi 4

#### Statistik suhu · Latihan 1 (pemanasan)

Mulai dari list ini:

```python
suhu = [28.5, 30.1, 27.8, 31.4, 29.0]
```

Tampilkan suhu tertinggi, suhu terendah, rata-rata (jumlah dibagi `len`), dan berapa banyak pembacaan yang lebih dari 30. Hasil yang diharapkan: tertinggi 31.4, terendah 27.8, rata-rata 29.36, dan jumlah di atas 30 ada 2. Petunjuk: pakai `round(rata_rata, 2)`.

Jawaban: [`Statistik suhu.py`](python/Sesi%204/Statistik%20suhu.py)

#### Daftar belanja · Latihan 2

Daftar alat belanja. Program terus meminta nama alat sampai pengguna mengetik `selesai`, lalu menampilkan daftar bernomor. Contoh jalannya:

```
Nama alat (ketik 'selesai' untuk berhenti): ESP32
Nama alat (ketik 'selesai' untuk berhenti): Breadboard
Nama alat (ketik 'selesai' untuk berhenti): selesai

Daftar belanja:
1. ESP32
2. Breadboard
Total: 2 alat
```

Petunjuk: gabungkan `while True`, `break`, `append`, dan `enumerate`. Kata `selesai` jangan sampai ikut masuk ke list.

Jawaban: [`Daftar belanja.py`](python/Sesi%204/Daftar%20belanja.py)

#### Data sensor · Latihan 3 (versi AIoT)

Mulai dari data ini:

```python
sensors = [
    {"id": "ESP32-01", "suhu": 29.5, "kelembapan": 65},
    {"id": "ESP32-02", "suhu": 33.2, "kelembapan": 58},
    {"id": "ESP32-03", "suhu": 31.0, "kelembapan": 72},
]
```

Program harus:

1. Menampilkan id semua sensor yang suhunya lebih dari 30.
2. Menghitung dan menampilkan rata-rata suhu seluruh sensor (dibulatkan 2 desimal).
3. Menambahkan kunci `"status"` ke tiap sensor: `"PANAS"` kalau suhu lebih dari 30, selain itu `"NORMAL"`, lalu menampilkan seluruh isi tiap dictionary.

Hasil yang diharapkan untuk dua poin pertama: id ESP32-02 dan ESP32-03, dan rata-rata 31.23.

Jawaban: [`Data sensor.py`](python/Sesi%204/Data%20sensor.py)

#### List baru berisi suhu di atas 30 · Tantangan (opsional)

Dari list suhu di Latihan 1, buat list baru berisi hanya pembacaan di atas 30, tanpa mengubah list aslinya.

Jawaban: [`List baru berisi suhu di atas 30.py`](python/Sesi%204/List%20baru%20berisi%20suhu%20di%20atas%2030.py)

### Sesi 5

#### Luas persegi panjang · Latihan 1 (pemanasan)

Buat fungsi `luas_persegi_panjang(panjang, lebar)` yang mengembalikan luasnya. Tes: `luas_persegi_panjang(5, 3)` harus menghasilkan 15.

Jawaban: [`Luas persegi panjang.py`](python/Sesi%205/Luas%20persegi%20panjang.py)

#### Konversi suhu · Latihan 2

Buat dua fungsi:

- `c_ke_f(c)`: Celsius ke Fahrenheit
- `f_ke_c(f)`: Fahrenheit ke Celsius, dengan rumus `(f - 32) * 5 / 9`

Tes: `c_ke_f(100)` → 212.0, `f_ke_c(212)` → 100.0, dan `f_ke_c(c_ke_f(37))` harus kembali ke sekitar 37 (bisa tampil 37.0 atau 36.99999... karena pembulatan pecahan).

Jawaban: [`Konversi suhu.py`](python/Sesi%205/Konversi%20suhu.py)

#### Pemantau ruang server · Latihan 3 (versi AIoT)

Buat tiga fungsi untuk memantau ruang server, lalu gabungkan.

- `rata_rata(data)`: mengembalikan rata-rata list, dibulatkan 2 desimal.
- `ringkasan(data)`: mengembalikan tiga nilai: terendah, tertinggi, rata-rata (pakai fungsi nomor 1).
- `status_ruang(suhu, kelembapan)`: mengembalikan teks `"BAHAYA"`, `"WASPADA"`, atau `"AMAN"`, dengan aturan yang sama seperti Sesi 2:
  - suhu lebih dari 35 atau kelembapan lebih dari 80 → BAHAYA
  - suhu 28 sampai 35 → WASPADA
  - selain itu → AMAN

Tes:

```python
data = [28.5, 30.1, 27.8, 31.4, 29.0]
terendah, tertinggi, rata = ringkasan(data)
print(terendah, tertinggi, rata)       # 27.8 31.4 29.36
print(status_ruang(30, 50))            # WASPADA
print(status_ruang(25, 90))            # BAHAYA
print(status_ruang(25, 50))            # AMAN
```

Jawaban: [`Pemantau ruang server.py`](python/Sesi%205/Pemantau%20ruang%20server.py)

#### Hitung nilai di atas ambang · Tantangan (opsional)

Buat fungsi `hitung_di_atas(data, ambang=30)` yang mengembalikan berapa banyak nilai di `data` yang lebih besar dari `ambang`. Dengan data yang sama: `hitung_di_atas(data)` harus 2, dan `hitung_di_atas(data, 29)` harus 3.

Jawaban: [`Hitung nilai di atas ambang.py`](python/Sesi%205/Hitung%20nilai%20di%20atas%20ambang.py)

### Sesi 6

#### baca suhu · Latihan 1 (pemanasan)

Baca file suhu. Buat file `suhu.txt` dengan isi (satu angka per baris):

```
28.5
30.1
27.8
31.4
29.0
```

Program membaca file itu dan menampilkan jumlah data, suhu tertinggi, dan rata-rata (2 desimal). Hasil yang diharapkan: 5, 31.4, 29.36. Tangani juga kasus file tidak ditemukan dengan pesan yang jelas. Tes dengan mengubah nama file di kode jadi nama yang salah.

Jawaban: [`baca suhu.py`](python/Sesi%206/baca%20suhu.py) (data: [`suhu.txt`](python/Sesi%206/suhu.txt))

#### input aman · Latihan 2

Input aman. Buat fungsi `minta_suhu()` yang terus meminta suhu sampai pengguna memasukkan angka yang valid dan antara -10 sampai 80. Kalau pengguna mengetik teks, tampilkan `Harus berupa angka.`; kalau angka di luar rentang, tampilkan `Di luar rentang -10 sampai 80.`. Fungsi mengembalikan angka yang valid.

Tes dengan urutan input `abc`, `200`, `25`. Seharusnya:

```
Suhu (C): abc
Harus berupa angka.
Suhu (C): 200
Di luar rentang -10 sampai 80.
Suhu (C): 25
```

dan fungsi mengembalikan 25.0. Ini gabungan dari Sesi 3 (`while True`), Sesi 5 (fungsi dengan `return`), dan sesi ini (`try` / `except`).

Jawaban: [`input aman.py`](python/Sesi%206/input%20aman.py)

#### pencatat data sensor · Latihan 3 (versi AIoT)

Pencatat data sensor. Buat program yang:

1. Menulis file `log.csv` dengan baris pertama (header) `waktu,suhu`, lalu 5 baris data berisi cap waktu saat ini dan suhu acak antara 25 dan 35 (dibulatkan 1 desimal). Pakai mode `"w"` supaya file dimulai bersih tiap dijalankan.
2. Setelah itu membaca file yang sama, melewati baris header, lalu menampilkan rata-rata suhu 5 data tadi.
3. Membungkus pembacaan file dengan `try` / `except FileNotFoundError`.

Karena suhunya acak, angka tiap orang akan berbeda, jadi cek hal-hal ini:

- File `log.csv` berisi 6 baris (1 header + 5 data).
- Rata-rata yang tampil berada di antara 25 dan 35.
- Tiap baris data berbentuk seperti `2026-11-02 14:30:05,29.4`.

Petunjuk: pakai `readlines()` lalu ambil `baris[1:]` untuk melewati header, dan `.split(",")` untuk mengambil kolom suhu.

Jawaban: [`pencatat data sensor.py`](python/Sesi%206/pencatat%20data%20sensor.py) (contoh hasil: [`log.csv`](python/Sesi%206/log.csv))

#### rata-rata aman · Tantangan (opsional)

Buat fungsi `rata_rata_aman(data)` yang mengembalikan `None` (bukan crash) kalau list kosong, memakai `try` / `except ZeroDivisionError`. Tes: `rata_rata_aman([])` harus `None`, dan `rata_rata_aman([2, 4])` harus 3.0.

Jawaban: [`rata-rata aman.py`](python/Sesi%206/rata-rata%20aman.py)

### Sesi 7

#### numpy dasar · Latihan 1 (pemanasan, NumPy)

Dari array ini:

```python
suhu = np.array([28.5, 30.1, 27.8, 31.4, 29.0])
```

Tampilkan: (a) suhu dalam Fahrenheit, dibulatkan 2 desimal dengan `np.round(..., 2)`, (b) tertinggi, terendah, dan rata-rata (2 desimal), (c) jumlah pembacaan di atas 30, dan (d) hanya nilai-nilai yang di atas 30.

Hasil yang diharapkan: tertinggi 31.4, terendah 27.8, rata-rata 29.36, jumlah di atas 30 ada 2, dan nilainya `[30.1 31.4]`. Nilai Fahrenheit kira-kira 83.3, 86.18, 82.04, 87.52, 84.2.

Jawaban: [`numpy dasar.py`](python/Sesi%207/numpy%20dasar.py)

#### Grafik dBm ke mW · Latihan 2 (versi telekom)

Grafik dBm ke mW. Buat array `dbm` dari -30 sampai 30 dengan langkah 5 (pakai `np.arange(-30, 31, 5)`), hitung `mw = 10 ** (dbm / 10)` untuk semuanya sekaligus tanpa perulangan, lalu gambar `mw` terhadap `dbm`. Gambar dua kali dalam satu program:

1. Grafik dengan sumbu y biasa.
2. Grafik yang sama, tapi tambahkan `plt.yscale("log")` sebelum `show`.

Lengkapi label sumbu dan judul, dan simpan keduanya sebagai `dbm_linear.png` dan `dbm_log.png`. Petunjuk: untuk gambar kedua, mulai dengan `plt.figure()` supaya tidak menimpa gambar pertama.

Yang harus terlihat: grafik pertama melengkung tajam naik di ujung kanan, sedangkan grafik kedua menjadi garis lurus. Itu alasan skala dB dipakai di telekomunikasi.

Jawaban: [`Grafik dBm ke mW.py`](python/Sesi%207/Grafik%20dBm%20ke%20mW.py) (hasil: [`dbm_linear.png`](python/Sesi%207/dbm_linear.png), [`dbm_log.png`](python/Sesi%207/dbm_log.png))

#### Rasio sinyal terhadap noise · Tantangan (opsional)

Dari kode sinyal + noise di materi, hitung rasio sederhana `np.mean(sinyal ** 2) / np.mean(noise ** 2)` untuk tiga tingkat noise (0,1, 0,5, 1,0), lalu tampilkan hasilnya. Semakin besar noise, semakin kecil rasionya. Itu gagasan awal di balik SNR.

Jawaban: [`Rasio sinyal terhadap noise.py`](python/Sesi%207/Rasio%20sinyal%20terhadap%20noise.py)

### Sesi 14-16

#### simulasi_adc · Latihan 3 (versi AIoT)

Dengan NumPy dan Matplotlib, buat `simulasi_adc.py`:

1. Buat sinyal sinus 5 Hz selama 1 detik, dicuplik 1000 Hz, yang bergerak antara 0 dan 3,3 V penuh (`x = 1.65 + 1.65 * np.sin(...)`).
2. Kuantisasi sinyal itu ke `N` bit: `kode = np.round(x / 3.3 * (2**N - 1))`, lalu kembalikan ke tegangan `xq = kode / (2**N - 1) * 3.3`.
3. Hitung SQNR hasil simulasi: `10 * log10(daya_sinyal / daya_error)`, dengan `daya_sinyal = np.var(x)` dan `daya_error = np.var(x - xq)`.
4. Lakukan untuk `N = 3, 4, 8, 12`, bandingkan dengan teori `6,02N + 1,76`, dan gambar sinyal asli vs hasil kuantisasi untuk `N = 3` pada satu grafik.

Hasil yang diharapkan: SQNR simulasi mendekati teori, yaitu sekitar 19,8 dB untuk 3 bit, 25,8 dB untuk 4 bit, 49,9 dB untuk 8 bit, dan 74,0 dB untuk 12 bit (selisih sekitar 1 dB masih wajar). Pada grafik 3-bit kamu akan melihat kurva berbentuk "tangga" yang mengikuti sinus.

Jawaban: [`simulasi_adc.py`](python/Sesi%2014-16/simulasi_adc.py)

---

## C

### Sesi 8

#### sesi8_1 · Latihan 1 (pemanasan)

Buat program yang meminta nama inisial (satu huruf) dan umur, lalu menampilkan: `Inisial: S, umur: 20`. Pakai `char` dan `int`. Petunjuk: untuk membaca `char` dengan `scanf`, tulis spasi sebelum penanda: `scanf(" %c", &inisial);`. Spasi itu membuang sisa baris baru dari input sebelumnya. Kalau kamu mengetik `S` dan `20`, hasilnya `Inisial: S, umur: 20`.

Jawaban: [`sesi8_1.c`](c/Sesi%208/sesi8_1.c)

#### sesi8_2 · Latihan 2

Program konversi suhu: minta suhu Celsius (`float`), tampilkan Fahrenheit dengan 1 desimal. Rumus `F = C * 9 / 5 + 32`. Tes: 0 menghasilkan 32.0, 100 menghasilkan 212.0, -40 menghasilkan -40.0. Setelah jalan, coba sengaja tulis rumusnya sebagai `C * (9 / 5) + 32` dengan semua variabel `int`, lalu amati hasilnya salah. Itu demonstrasi jebakan pembagian bulat: `9 / 5` jadi 1, bukan 1.8.

Jawaban: [`sesi8_2.c`](c/Sesi%208/sesi8_2.c)

#### sesi8_3 · Latihan 3 (versi telekom/AIoT)

Program yang meminta daya dalam dBm, lalu menampilkan dayanya dalam mW. Pakai `pow()` dan `math.h`, dengan kompilasi memakai `-lm` kalau perlu. Tes: 0 menghasilkan `1.000000 mW`, -30 menghasilkan `0.001000 mW`, dan 20 menghasilkan `100.000000 mW`. Lalu tambahkan: tampilkan juga pembulatan 2 desimal dengan `%.2f`.

Jawaban: [`sesi8_3.c`](c/Sesi%208/sesi8_3.c)

#### sesi8_4 · Tantangan (opsional)

Minta pengguna memasukkan dua bilangan bulat, lalu tampilkan hasil bagi dengan tiga cara: pembagian bulat, pembagian desimal dengan casting, dan sisa bagi. Untuk 7 dan 2: 3, 3.5, dan 1.

Jawaban: [`sesi8_4.c`](c/Sesi%208/sesi8_4.c)

### Sesi 9

#### sesi9_1 · Latihan 1 (pemanasan)

Genap/ganjil dan pembagian aman. Minta dua bilangan bulat `a` dan `b`. Tampilkan apakah `a` genap atau ganjil. Lalu, hanya kalau `b` tidak nol, tampilkan `a / b` (bulat) dan sisa `a % b`; kalau `b` nol, tampilkan `Tidak bisa dibagi nol`. Tes:

| a | b | Yang muncul |
|---|---|---|
| 7 | 2 | Ganjil, lalu `7 / 2 = 3`, `7 % 2 = 1` |
| 10 | 5 | Genap, lalu `10 / 5 = 2`, `10 % 5 = 0` |
| 4 | 0 | Genap, lalu `Tidak bisa dibagi nol` |

Jawaban: [`sesi9_1.c`](c/Sesi%209/sesi9_1.c)

#### sesi9_2 · Latihan 2

Menu konversi dengan `switch`. Program menampilkan menu: 1 = Celsius ke Fahrenheit, 2 = Fahrenheit ke Celsius, 3 = dBm ke mW. Pengguna memilih nomor, memasukkan nilainya, dan program menampilkan hasil. Nomor lain menampilkan `Pilihan tidak valid`. Gunakan `switch` dengan `break` di setiap `case`. Tes:

| Pilihan | Nilai | Hasil |
|---|---|---|
| 1 | 100 | 212.0 F |
| 2 | 212 | 100.0 C |
| 3 | 20 | 100.000000 mW |
| 9 | (tidak ada) | Pilihan tidak valid |

Jawaban: [`sesi9_2.c`](c/Sesi%209/sesi9_2.c)

#### sesi9_3 · Latihan 3 (versi AIoT)

Alarm ruang server dan input aman. Gabungkan dua hal:

1. Minta suhu dan kelembapan, tapi terus minta lagi sampai input valid: harus berupa angka, suhu dalam -10 sampai 80, dan kelembapan dalam 0 sampai 100. Pakai pola `scanf` dengan nilai kembalian.
2. Setelah valid, tampilkan status dengan aturan yang sama seperti Sesi 2: suhu lebih dari 35 atau kelembapan lebih dari 80 → BAHAYA; suhu dari 28 sampai 35 (inklusif) → WASPADA; selain itu → AMAN. Ingat: tidak boleh pakai `28 <= suhu <= 35`.

Tes (status):

| Suhu | Kelembapan | Seharusnya |
|---|---|---|
| 25 | 50 | AMAN |
| 30 | 50 | WASPADA |
| 40 | 50 | BAHAYA |
| 25 | 90 | BAHAYA |
| 35 | 80 | WASPADA |

Tes validasi: ketik `abc`, lalu `200`, lalu `25` untuk suhu. Dua yang pertama harus ditolak (pesan `Harus berupa angka.` dan `Di luar rentang -10 sampai 80.`), dan 25 diterima.

Jawaban: [`sesi9_3.c`](c/Sesi%209/sesi9_3.c)

#### sesi9_4 · Tantangan (opsional)

Pakai `for` untuk menghitung jumlah bilangan 1 sampai `n` (dari input), lalu pakai `continue` untuk menjumlahkan hanya bilangan ganjil. Untuk n = 10: jumlah semua = 55, dan jumlah ganjil saja (1+3+5+7+9) = 25.

Jawaban: [`sesi9_4.c`](c/Sesi%209/sesi9_4.c)

### Sesi 10

#### sesi10_1 · Latihan 1 (pemanasan)

Statistik array. Dari array ini:

```c
float suhu[] = {28.5f, 30.1f, 27.8f, 31.4f, 29.0f};
```

Hitung panjangnya dengan `sizeof`, lalu tampilkan: tertinggi, terendah, rata-rata (2 desimal), dan jumlah pembacaan di atas 30. Hasil yang diharapkan: tertinggi 31.4, terendah 27.8, rata-rata 29.36, jumlah di atas 30 ada 2. Petunjuk: mulai tertinggi dan terendah dari `suhu[0]`, lalu bandingkan dari indeks 1.

Jawaban: [`sesi10_1.c`](c/Sesi%2010/sesi10_1.c)

#### sesi10_2 · Latihan 2

Panjang, terbalik, dan palindrom. Minta satu kata (maksimal 19 karakter, pakai `scanf("%19s", ...)`). Tampilkan panjangnya, kata dalam urutan terbalik, dan apakah kata itu palindrom (dibaca sama dari depan dan belakang). Tes:

| Kata | Yang muncul |
|---|---|
| ESP32 | panjang 5, terbalik `23PSE`, Bukan palindrom |
| katak | panjang 5, terbalik `katak`, Palindrom |
| Kayak | panjang 5, terbalik `kayaK`, Bukan palindrom |

Baris terakhir sengaja: karena `strcmp` dan perbandingan karakter membedakan huruf besar dan kecil, `Kayak` dianggap bukan palindrom di program dasar ini. Petunjuk: bangun array kedua yang berisi kata terbalik dengan perulangan, lalu bandingkan dengan `strcmp(...) == 0`. Jangan lupa menutup array hasil dengan `'\0'`.

Jawaban: [`sesi10_2.c`](c/Sesi%2010/sesi10_2.c)

#### sesi10_3 · Latihan 3 (versi AIoT)

Log suhu sepanjang hari. Pakai data per jam ini (jam 8 sampai 17):

```c
float suhu[] = {26.5f, 27.0f, 28.2f, 29.5f, 31.0f, 32.4f, 33.1f, 32.0f, 30.2f, 28.8f};
```

Program harus:

1. Menampilkan tabel `Jam 08: 26.5 C` dan seterusnya sampai jam 17 (jam dua digit).
2. Mencari suhu tertinggi dan jam saat itu terjadi.
3. Menghitung rata-rata dan jumlah jam di atas 30.
4. Membentuk topik MQTT dengan `snprintf` untuk sensor nomor 1: `lab/esp32-01/suhu`, lalu mencetaknya.

Hasil yang diharapkan: tertinggi 33.1 pada jam 14, rata-rata 29.87, jumlah jam di atas 30 ada 5 (jam 12, 13, 14, 15, 16), dan topik `lab/esp32-01/suhu`.

Jawaban: [`sesi10_3.c`](c/Sesi%2010/sesi10_3.c)

#### sesi10_4 · Tantangan (opsional)

Membalik array di tempat. Dari `int a[] = {1, 2, 3, 4, 5};`, balikkan isinya di array yang sama (tanpa array kedua) dengan menukar elemen pertama dan terakhir, lalu kedua dan kedua dari belakang, dan seterusnya. Tampilkan hasilnya: `5 4 3 2 1`. Petunjuk: perulangan hanya sampai setengah panjang, dan butuh variabel sementara untuk menukar.

Jawaban: [`sesi10_4.c`](c/Sesi%2010/sesi10_4.c)

### Sesi 11

#### sesi11_1 · Latihan 1 (pemanasan)

Fungsi dengan prototype. Buat tiga fungsi dan tulis prototype-nya di atas `main`, definisinya di bawah:

```c
int luas(int panjang, int lebar)
float c_ke_f(float c)
float f_ke_c(float f)
```

Panggil dari `main` dan tampilkan hasilnya. Tes:

| Panggilan | Hasil |
|---|---|
| `luas(5, 3)` | 15 |
| `c_ke_f(100)` | 212.0 |
| `f_ke_c(212)` | 100.0 |
| `f_ke_c(c_ke_f(-40))` | -40.0 |

Jawaban: [`sesi11_1.c`](c/Sesi%2011/sesi11_1.c)

#### sesi11_2 · Latihan 2

Pointer. Dua bagian dalam satu program:

1. Buat `void tukar(int *a, int *b)`. Mulai dari `x = 3`, `y = 7`, tukar, lalu tampilkan. Hasil yang diharapkan: `x = 7`, `y = 3`.
2. Buat `void ringkasan(const float data[], int n, float *kecil, float *besar, float *rata)`. Pakai array `{28.5f, 30.1f, 27.8f, 31.4f, 29.0f}`. Hasil yang diharapkan: terendah 27.8, tertinggi 31.4, rata-rata 29.36.

Setelah jalan, lakukan percobaan: panggil `tukar(x, y)` tanpa `&`, dan lihat apa yang dikatakan compiler (dengan `-Wall`). Itu cara terbaik mengenali pesan error-nya.

Jawaban: [`sesi11_2.c`](c/Sesi%2011/sesi11_2.c)

#### sesi11_3 · Latihan 3 (versi AIoT)

Struct sensor. Pakai data ini:

```c
Sensor sensors[3] = {
    {"ESP32-01", 25.0f, 50.0f},
    {"ESP32-02", 33.2f, 58.0f},
    {"ESP32-03", 38.0f, 85.0f}
};
```

Buat fungsi `const char *status(const Sensor *s)` (aturan sama seperti Sesi 2: BAHAYA kalau suhu > 35 atau kelembapan > 80, WASPADA kalau suhu 28 sampai 35 inklusif, selain itu AMAN), fungsi `float rata_suhu(const Sensor s[], int n)`, dan fungsi `void naikkan_suhu(Sensor *s, float delta)`. Program menampilkan:

```
ESP32-01: 25.0 C, 50.0 %, AMAN
ESP32-02: 33.2 C, 58.0 %, WASPADA
ESP32-03: 38.0 C, 85.0 %, BAHAYA
Rata-rata suhu: 32.07
```

Lalu panggil `naikkan_suhu(&sensors[0], 5.0f)` dan tampilkan lagi sensor pertama. Hasil yang diharapkan: `ESP32-01: 30.0 C, 50.0 %, WASPADA`.

Petunjuk: untuk mencetak tanda persen, tulis `%%`. Format cetaknya: `"%s: %.1f C, %.1f %%, %s\n"`.

Jawaban: [`sesi11_3.c`](c/Sesi%2011/sesi11_3.c)

#### sesi11_4 · Tantangan (opsional)

Hitung status lewat pointer. Buat `void hitung_status(const Sensor s[], int n, int *aman, int *waspada, int *bahaya)` yang menghitung berapa sensor di tiap status. Dengan data di Latihan 3 (sebelum `naikkan_suhu`), hasilnya aman = 1, waspada = 1, bahaya = 1. Panggil fungsi `status` dari dalamnya, dan bandingkan hasilnya dengan `strcmp(...) == 0`.

Jawaban: [`sesi11_4.c`](c/Sesi%2011/sesi11_4.c)

---

## Linux

#### laporan · Latihan 3 (versi AIoT)

Dengan `nano`, buat skrip `laporan.sh` yang menerima nama file sebagai argumen. Skrip menampilkan jumlah data, suhu terendah, dan suhu tertinggi. Tambahkan dua penanganan: kalau argumen kosong, tampilkan `Pemakaian: ./laporan.sh namafile` dan keluar dengan kode 1, dan kalau file tidak ada, tampilkan `File tidak ditemukan: <nama>`.

Setelah itu `chmod +x laporan.sh` dan uji:

| Perintah | Seharusnya |
|---|---|
| `./laporan.sh suhu.txt` | Jumlah data: 5, Terendah: 27.8, Tertinggi: 31.4 |
| `./laporan.sh` | Pemakaian: ./laporan.sh namafile |
| `./laporan.sh tidakada.txt` | File tidak ditemukan: tidakada.txt |

Jawaban: [`laporan.sh`](linux/laporan.sh)
