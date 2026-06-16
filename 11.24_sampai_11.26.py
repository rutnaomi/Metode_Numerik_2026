# Rut Naomi E.S || F55123057
# Untuk soal 11.24 sampai 11.26: Program User-Friendly untuk Thomas Algorithm
import numpy as np

# 11.24 PROGRAM USER-FRIENDLY THOMAS ALGORITHM

def thomas_user_friendly():
    print("\n--- PROGRAM THOMAS ALGORITHM ---")
    print("Program ini digunakan untuk menyelesaikan matriks tridiagonal.")
    # Secara ideal, di sini ada fungsi input(), namun untuk 
    # kemudahan eksekusi otomatis, saya simulasikan parameternya:
    
    # Test Data menggunakan matriks dari Soal 11.1
    a = np.array([-0.4, -0.4])          # Sub-diagonal
    b = np.array([0.8, 0.8, 0.8])       # Diagonal utama
    c = np.array([-0.4, -0.4])          # Super-diagonal
    d = np.array([41.0, 25.0, 105.0])   # Vektor hasil
    
    n = len(d)
    c_star = np.zeros(n-1); d_star = np.zeros(n); x = np.zeros(n)
    
    c_star[0] = c[0] / b[0]
    d_star[0] = d[0] / b[0]
    for i in range(1, n-1):
        c_star[i] = c[i] / (b[i] - a[i-1] * c_star[i-1])
    for i in range(1, n):
        d_star[i] = (d[i] - a[i-1] * d_star[i-1]) / (b[i] - a[i-1] * c_star[i-1])

    x[-1] = d_star[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_star[i] - c_star[i] * x[i+1]
        
    print(f"-> Hasil Solusi Thomas: {np.round(x, 4)}")

# 11.25 PROGRAM USER-FRIENDLY CHOLESKY DECOMPOSITION
def cholesky_user_friendly():
    print("\n--- PROGRAM CHOLESKY DECOMPOSITION ---")
    print("Pastikan matriks yang Anda masukkan adalah Simetris dan Positif Definit.")
    
    # Test Data menggunakan matriks dari Soal 11.7
    A = np.array([
        [9.0, 0.0, 0.0],
        [0.0, 25.0, 0.0],
        [0.0, 0.0, 4.0]
    ])
    
    n = A.shape[0]
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = np.sqrt(A[i][i] - sum_k)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - sum_k))
                
    print("-> Matriks [L] Hasil Cholesky:")
    print(np.round(L, 4))

# 11.26 PROGRAM USER-FRIENDLY GAUSS-SEIDEL
def gauss_seidel_user_friendly():
    print("\n--- PROGRAM GAUSS-SEIDEL ---")
    print("Pastikan sistem Anda Diagonally Dominant agar dapat konvergen.")
    
    # Test Data menggunakan matriks dari Soal 11.11
    A = np.array([
        [ 10.0,   2.0,  -1.0],
        [ -3.0,  -6.0,   2.0],
        [  1.0,   1.0,   5.0]
    ])
    b = np.array([27.0, -61.5, -21.5])
    
    tol = 5.0 # Batas toleransi 5%
    max_iter = 100
    n = len(b)
    x = np.zeros(n)
    
    for iter_count in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            sum_val = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_val) / A[i][i]
            
        ea = np.max(np.abs((x - x_old) / x)) * 100
        if ea < tol:
            print(f"-> Konvergen pada iterasi ke-{iter_count}")
            print(f"-> Solusi X: {np.round(x, 4)} dengan error maks {ea:.2f}%")
            return
            
    print("-> Gagal konvergen dalam batas iterasi maksimum.")

# Eksekusi Program
print("=== Soal 11.24 - 11.26: User-Friendly Programs ===")
thomas_user_friendly()
cholesky_user_friendly()
gauss_seidel_user_friendly()