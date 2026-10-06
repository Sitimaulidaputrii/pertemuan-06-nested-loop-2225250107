# Loop luar mengatur nilai i dari 1 sampai 4.
# Loop dalam mengatur nilai j dari 1 sampai 3.
# total_baris digunakan untuk menjumlahkan nilai i * j pada setiap baris.
# Output menampilkan jumlah setiap baris.

for i in range(1, 5):
    total_baris = 0 

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}") 