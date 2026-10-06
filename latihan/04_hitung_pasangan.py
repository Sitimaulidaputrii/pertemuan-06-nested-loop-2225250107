# Loop luar mengatur nilai i dari 1 sampai n.
# Loop dalam mengatur nilai j dari 1 sampai n.
# Kondisi memeriksa apakah i + j <= n.
# count digunakan sebagai counter untuk menghitung pasangan yang memenuhi kondisi.
# Output menampilkann banyak pasangan yang memenuhi kondisi.

n = int(input("n: "))
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan: {count}")  