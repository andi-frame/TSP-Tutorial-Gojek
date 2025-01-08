import itertools

# Fungsi untuk menghitung total klik (bobot) untuk sebuah urutan
def calculate_total_clicks(order, dist_matrix):
    total_clicks = 0
    for i in range(len(order) - 1):
        total_clicks += dist_matrix[order[i]][order[i+1]]
    total_clicks += dist_matrix[order[-1]][order[0]]  # Kembali ke titik awal
    return total_clicks

# Fungsi untuk mencari jalur optimal menggunakan algoritma brute force
def tsp_bruteforce(dist_matrix):
    # Membuat semua kemungkinan urutan
    n = len(dist_matrix)
    all_permutations = itertools.permutations(range(n))
    
    # Menyimpan hasil terbaik
    min_clicks = float('inf')
    best_order = None
    
    # Memeriksa setiap permutasi untuk menemukan urutan terbaik
    for order in all_permutations:
        total_clicks = calculate_total_clicks(order, dist_matrix)
        if total_clicks < min_clicks:
            min_clicks = total_clicks
            best_order = order
    
    return best_order, min_clicks

# Matriks jarak (jumlah klik) antar fitur aplikasi
dist_matrix = [
    [0, 2, 9, 10, 1],  # Fitur A
    [2, 0, 6, 4, 3],   # Fitur B
    [9, 6, 0, 3, 7],   # Fitur C
    [10, 4, 3, 0, 8],  # Fitur D
    [1, 3, 7, 8, 0],   # Fitur E
]

# Menjalankan fungsi TSP untuk mencari urutan optimal
best_order, min_clicks = tsp_bruteforce(dist_matrix)

# Menampilkan hasil
print("Urutan optimal fitur aplikasi (indeks fitur):", best_order)
print("Total klik (waktu yang dibutuhkan):", min_clicks)


features = ['Pemesanan Makanan', 'Transportasi', 'Pengiriman Barang', 'Pembayaran', 'Akun Pengguna']
optimal_order_features = [features[i] for i in best_order]

print("Urutan optimal fitur aplikasi:", optimal_order_features)
