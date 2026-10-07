# Pertemuan 06 Nested Loop Python

Nama: Siti Maulida Putri Irawan
NIM: 2225250107
Kelas: 3A

## Tujuan

Praktik ini bertujuan untuk memahami dan menerapkan konsep nested loop menggunakan Python. Nested loop digunakan untuk menjalankan sebuah perulangan di dalam perulangan lainnya. Melalui latihan dan tugas yang diberikan, konsep nested loop diterapkan untuk membuat pola, menghitung pasangan nilai, melakukan akumulasi, serta melakukan pencacahan.

## Cara Menjalankan

Program tugas dapat dijalankan melalui Terminal VS Code dengan perintah:
```bash
python tugas/tabel_perkalian_dan_statistik_py
```

Untuk menjalankan program latihan:
```bash
python latihan/01_pasangan_indeks.py
```

Untuk menjalankan yang lainnya, gunakan perintah sesuai dengan nama berkasnya.

## Algoritma Tugas 3

1. Masukkan nilai n.
2. periksa nilai n. jika n <= 0, maka masukkan kembali nilai sampai nilainya positif.
3. Atur nilai total_nilai = 0 dan count_genap = 0.
4. Gunakan perulangan for untuk nilai i dari 1 sampai n.
5. Atur nilai total_baris = 0 untuk setiap nilai i.
6. Gunakan perulangan for untuk nilai j dari 1 sampai n.
7. Hitung hasil perkalian dengan rumus hasil = i × j.
8. Tampilkan hasil, kemudian tambahkan nilainya ke total_baris dan total_semua.
9. Periksa hasil, jika hasilnya genap, tambahkan count_genap sebanyak 1.
10. Setelah perulangan dalam selesai, tampilkan total_baris.
11. Setelah seluruh perulangan selesai, tampilkan total_semua dan count_genap.

## Hasil Pengujian

| Input (n) | Hasil yang diharapkan | Keluaran Aktual | Status |
| --- | --- | --- | --- | 
| 1 | Jumlah pasangan: 1, total: 1, hasil genap: 0 | Jumlah pasangan: 1, total: 1, hasil genap: 0 | Berhasil |
| 2 | Jumlah pasangan: 4, total: 9, hasil genap: 3 | Jumlah pasangan: 4, total: 9, hasil genap: 3 | Berhasil |
| 3 | Jumlah pasangan: 9, total: 36, hasil genap: 5 | Jumlah pasangan: 9, total: 36, hasil genap: 5 | Berhasil |

Pengujian dilakukan menggunakan beberapa nilai n untuk memastikan program dapat menghasilkan tabel perkalian, jumlah setiap baris, total seluruh hasil, dan jumlah hasil genap dengan benar.

## Analisis Efisiensi

Untuk input n, loop luar berjalan sebanyak n kali. Pada setiap iterasi loop luar, loop dalam juga berjalan sebanyak n kali. Oleh karena itu, badan loop dalam berjalan sebanyak n × n atau n² kali. Misalnya, untuk n = 3, badan loop dalam berjalan sebanyak 3 × 3 = 9 kali.

## Refleksi

Pada pertemuan 06, saya belajar lebih memahami cara kerja nested loop, terutama hubungan antara loop luar dan loop dalam. Salah satu kesalahan yang saya temukan adalah menempatkan total_baris = 0 pada posisi yang salah. Kesalahan tersebut diperbaiki dengan menempatkan total_baris = 0 di dalam loop luar sebelum loop dalam dimulai. Dari proses ini, saya jadi memahami bahwa posisi suatu variabel dalam nested loop dapat mempengaruhi hasil program. Saya juga jadi lebih memahami penggunaan akumulator untuk menjumlahkan hasil dan counter untuk menghitung banyaknya hasil yang memenuhi kondisi.

## Sumber

Materi pertemuan 06 Algoritma dan Pemrograman: Nested loop, Pola, Akumulasi, dan Pencacahan dalam Python di VS Code dan Pengumpulan melalui GitHub