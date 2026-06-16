# Rut Naomi E.S || F55123057
# Untuk soal 11.8 sampai 11.13
# Yang ini metode Iteratif Gauss-Seidel dan Jacobi
import numpy as np

# fungsi utama untuk metode iteratif
def iterasi_sistem(A, b, metode='gauss_seidel', es=5.0, max_iter=100, lam=1.0):
    """
    Menyelesaikan sistem persamaan linear menggunakan metode iteratif.
    metode: 'gauss_seidel' atau 'jacobi'
    es: kriteria penghentian error relatif persen (default 5%)
    lam: faktor relaksasi (default 1.0 = tanpa relaksasi)
    """
    n = len(b)
    x = np.zeros(n)
    x_old = np.zeros(n)
    
    for iteration in range(1, max_iter + 1):
        x_old[:] = x[:]
        
        for i in range(n):
            # Jumlahkan elemen selain diagonal utama
            if metode == 'gauss_seidel':
                sum_val = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            else: # jacobi
                sum_val = np.dot(A[i, :i], x_old[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
                
            # Hitung nilai x baru
            x_new = (b[i] - sum_val) / A[i, i]
            
            # Terapkan relaksasi
            x[i] = lam * x_new + (1 - lam) * x_old[i]
            
        # Hitung error relatif hampiran (ea)
        ea = np.zeros(n)
        for i in range(n):
            if x[i] != 0:
                ea[i] = abs((x[i] - x_old[i]) / x[i]) * 100
                
        # Cek kriteria konvergensi (maksimum error dari semua elemen < es)
        if np.max(ea) < es:
            return x, iteration, np.max(ea)
            
    return x, max_iter, np.max(ea)

# eksekusi soal nomor 11.8
print("=== Soal 11.8 (Gauss-Seidel + Overrelaxation) ===")
# Matriks dari soal 11.1
A_11_8 = np.array([
    [ 0.8, -0.4,  0.0],
    [-0.4,  0.8, -0.4],
    [ 0.0, -0.4,  0.8]
])
b_11_8 = np.array([41.0, 25.0, 105.0])

x_11_8, iter_11_8, ea_11_8 = iterasi_sistem(A_11_8, b_11_8, metode='gauss_seidel', es=5.0, lam=1.2)
print(f"Solusi: {np.round(x_11_8, 4)}")
print(f"Selesai dalam {iter_11_8} iterasi dengan max error {ea_11_8:.2f}%\n")

# eksekusi soal nomor 11.9 & 11.10

print("=== Soal 11.9 (Gauss-Seidel) & 11.10 (Jacobi) ===")
A_11_9 = np.array([
    [ 15.0,  -3.0,  -1.0],
    [ -3.0,  18.0,  -6.0],
    [ -4.0,  -1.0,  12.0]
])
b_11_9 = np.array([3800.0, 1200.0, 2350.0])

x_11_9, iter_11_9, ea_11_9 = iterasi_sistem(A_11_9, b_11_9, metode='gauss_seidel', es=5.0)
print(f"[11.9] Gauss-Seidel -> Solusi: {np.round(x_11_9, 4)} (Iterasi: {iter_11_9}, Err: {ea_11_9:.2f}%)")

x_11_10, iter_11_10, ea_11_10 = iterasi_sistem(A_11_9, b_11_9, metode='jacobi', es=5.0)
print(f"[11.10] Jacobi      -> Solusi: {np.round(x_11_10, 4)} (Iterasi: {iter_11_10}, Err: {ea_11_10:.2f}%)\n")

# eksekusi soal nomor 11.11
print("=== Soal 11.11 (Gauss-Seidel) ===")
A_11_11 = np.array([
    [ 10.0,   2.0,  -1.0],
    [ -3.0,  -6.0,   2.0],
    [  1.0,   1.0,   5.0]
])
b_11_11 = np.array([27.0, -61.5, -21.5])

x_11_11, iter_11_11, ea_11_11 = iterasi_sistem(A_11_11, b_11_11, metode='gauss_seidel', es=5.0)
print(f"Solusi: {np.round(x_11_11, 4)}")
print(f"Selesai dalam {iter_11_11} iterasi dengan max error {ea_11_11:.2f}%\n")

# eksekusi soal nomor 11.12

print("=== Soal 11.12 (Penting: Rearrange Matriks) ===")
# Soal menginstruksikan "If necessary, rearrange the equations to achieve convergence"
# Kita harus membuat matriks Dominan secara Diagonal
A_11_12_rearranged = np.array([
    [  6.0,  -1.0,  -1.0], # Persamaan ke-2 (6x1 dominan)
    [  6.0,   9.0,   1.0], # Persamaan ke-3 (9x2 dominan)
    [ -3.0,   1.0,  12.0]  # Persamaan ke-1 (12x3 dominan)
])
b_11_12_rearranged = np.array([3.0, 40.0, 50.0])

# (a) Tanpa Relaksasi
x_11_12a, iter_11_12a, _ = iterasi_sistem(A_11_12_rearranged, b_11_12_rearranged, es=5.0, lam=1.0)
print(f"(a) Tanpa Relaksasi: {np.round(x_11_12a, 4)} (Iterasi: {iter_11_12a})")

# (b) Dengan Relaksasi (lam = 0.95)
x_11_12b, iter_11_12b, _ = iterasi_sistem(A_11_12_rearranged, b_11_12_rearranged, es=5.0, lam=0.95)
print(f"(b) Dengan Relaksasi (0.95): {np.round(x_11_12b, 4)} (Iterasi: {iter_11_12b})\n")


# eksekusi soal nomor 11.13

print("=== Soal 11.13 (Penting: Rearrange Matriks) ===")
# Sama seperti 11.12, kita harus mengatur persamaannya agar dominan di diagonal
A_11_13_rearranged = np.array([
    [ -8.0,   1.0,  -2.0], # Persamaan ke-3 (-8x1 dominan)
    [  2.0,  -6.0,  -1.0], # Persamaan ke-1 (-6x2 dominan)
    [ -3.0,  -1.0,   7.0]  # Persamaan ke-2 (7x3 dominan)
])
b_11_13_rearranged = np.array([-20.0, -38.0, -34.0])

# (a) Tanpa Relaksasi
x_11_13a, iter_11_13a, _ = iterasi_sistem(A_11_13_rearranged, b_11_13_rearranged, es=5.0, lam=1.0)
print(f"(a) Tanpa Relaksasi: {np.round(x_11_13a, 4)} (Iterasi: {iter_11_13a})")

# (b) Dengan Relaksasi (lam = 1.2)
x_11_13b, iter_11_13b, _ = iterasi_sistem(A_11_13_rearranged, b_11_13_rearranged, es=5.0, lam=1.2)
print(f"(b) Dengan Relaksasi (1.2): {np.round(x_11_13b, 4)} (Iterasi: {iter_11_13b})")