# Rut Naomi E.S || F55123057
# Untuk soal 11.4 sampai 11.7

import numpy as np

def solve_cholesky(A, b):
    """
    Menyelesaikan sistem persamaan linear Ax = b menggunakan Dekomposisi Cholesky.
    Mengembalikan matriks L dan vektor solusi x.
    """
    # 1. Dekomposisi Cholesky: A = L * L.T
    L = np.linalg.cholesky(A)
    
    # 2. Forward substitution: L * y = b
    y = np.linalg.solve(L, b)
    
    # 3. Backward substitution: L.T * x = y
    x = np.linalg.solve(L.T, y)
    
    return L, x

def check_cholesky_validity(A, L):
    """
    Memvalidasi apakah L * L^T menghasilkan matriks A kembali (Soal 11.4).
    """
    A_reconstructed = np.dot(L, L.T)
    # np.allclose mengecek apakah kedua matriks sama dalam batas toleransi numerik
    is_valid = np.allclose(A, A_reconstructed)
    return is_valid, A_reconstructed

# eksekusi soal nomor 11.5

print("=== Hasil Soal 11.5 ===")
# Matriks dari soal 11.5
A_11_5 = np.array([
    [6.0, 15.0, 55.0],
    [15.0, 55.0, 225.0],
    [55.0, 225.0, 979.0]
])
b_11_5 = np.array([152.6, 585.6, 2488.8])

L_11_5, a_11_5 = solve_cholesky(A_11_5, b_11_5)
print("Matriks L (Dekomposisi Cholesky):")
print(np.round(L_11_5, 4))
print("\nSolusi vektor a:")
print(np.round(a_11_5, 4))

# eksekusi Soal 11.4 menggunakan matriks dari Soal 11.5 sebagai contoh
print("\n=== Hasil Soal 11.4 (Validasi Example) ===")
is_valid, A_rec = check_cholesky_validity(A_11_5, L_11_5)
print(f"Apakah [L][L]^T == [A]? {is_valid}")


# eksekusi soal nomor 11.6

print("\n=== Hasil Soal 11.6 ===")
# Matriks dari soal 11.6
A_11_6 = np.array([
    [8.0, 20.0, 15.0],
    [20.0, 80.0, 50.0],
    [15.0, 50.0, 60.0]
])
b_11_6 = np.array([50.0, 250.0, 100.0])

L_11_6, x_11_6 = solve_cholesky(A_11_6, b_11_6)
print("Matriks L (Dekomposisi Cholesky):")
print(np.round(L_11_6, 4))
print("\nSolusi vektor x:")
print(np.round(x_11_6, 4))

# eksekusi soal nomor 11.7
print("\n=== Hasil Soal 11.7 ===")
# Matriks diagonal dari soal 11.7
A_11_7 = np.array([
    [9.0, 0.0, 0.0],
    [0.0, 25.0, 0.0],
    [0.0, 0.0, 4.0]
])

# Karena tidak ada vektor b yang diminta, kita hanya mencari dekomposisinya
L_11_7 = np.linalg.cholesky(A_11_7)
print("Matriks L (Dekomposisi Cholesky):")
print(L_11_7)
print("\nPenjelasan Soal 11.7:")
print("Sesuai dengan persamaan (11.3) dan (11.4), hasil ini sangat masuk akal.")
print("Untuk matriks diagonal murni, dekomposisi Cholesky [L] hanyalah matriks")
print("diagonal baru di mana setiap elemennya adalah akar kuadrat dari")
print("elemen diagonal matriks [A] yang asli (akar dari 9, 25, dan 4).")