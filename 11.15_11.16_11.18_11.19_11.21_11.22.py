# Rut Naomi E.S || F55123057
# Untuk Soal 11.15, 11.16, 11.18, 11.19, 11.21, 11.22

import numpy as np
import scipy.linalg as la

print("=== Soal 11.15: Uji Konvergensi Gauss-Seidel ===")
# Set 3 adalah set yang sulit/tidak akan konvergen karena matriksnya tidak bisa 
# disusun menjadi diagonally dominant (dominan secara diagonal).
A_set3 = np.array([
    [-1,  3,  5],
    [ 2,  4, -5],
    [ 0,  2, -1]
])
print("Matriks Set 3 tidak diagonally dominant. Jika Gauss-Seidel dipaksakan,")
print("nilai error relatifnya akan terus membesar (divergen) seiring bertambahnya iterasi.\n")

print("=== Soal 11.16: Inverse & Condition Number (Row-Sum Norm) ===")
A_11_16 = np.array([
    [ 1,  4,  9, 16],
    [ 4,  9, 16, 25],
    [ 9, 16, 25, 36],
    [16, 25, 36, 49]
])
b_11_16 = np.array([30, 54, 86, 126])
x_11_16 = np.linalg.solve(A_11_16, b_11_16)
inv_11_16 = np.linalg.inv(A_11_16)
cond_11_16 = np.linalg.cond(A_11_16, p=np.inf) # p=np.inf adalah Row-Sum Norm
print(f"Solusi x: {np.round(x_11_16, 2)}")
print(f"Condition Number (Row-sum): {cond_11_16:.2f}\n")

print("=== Soal 11.18: Produksi Komponen Elektronik ===")
# T = Transistor, R = Resistor, C = Chip
# Copper: 4T + 3R + 2C = 960
# Zinc:   1T + 3R + 1C = 510
# Glass:  2T + 1R + 3C = 610
A_11_18 = np.array([[4, 3, 2], [1, 3, 1], [2, 1, 3]])
b_11_18 = np.array([960, 510, 610])
x_11_18 = np.linalg.solve(A_11_18, b_11_18)
print(f"Produksi -> Transistor: {x_11_18[0]:.0f}, Resistor: {x_11_18[1]:.0f}, Chips: {x_11_18[2]:.0f}\n")

print("=== Soal 11.19: Condition Number Matriks Hilbert 10x10 ===")
H_10 = la.hilbert(10)
cond_hilbert = np.linalg.cond(H_10, p=2) # Spectral condition number
print(f"Spectral Condition Number Hilbert 10x10: {cond_hilbert:.5e}")
print("Digit presisi yang hilang diperkirakan sekitar log10(Condition Number).")
print(f"Perkiraan digit hilang: {np.log10(cond_hilbert):.2f} digit.\n")

print("=== Soal 11.21: Perintah Matriks Augmented ===")
A_contoh = np.array([[1, 2], [3, 4]])
Aug = np.hstack((A_contoh, np.eye(A_contoh.shape[0])))
print("Perintah Python: Aug = np.hstack((A, np.eye(len(A))))")
print(f"Hasil:\n{Aug}\n")

print("=== Soal 11.22: Rearrange Matrix ===")
# Setelah disusun ulang variabel x1, x2, x3 ke sisi kiri:
A_11_22 = np.array([
    [ 0, -7,  5],
    [ 4,  0,  7],
    [-4,  3, -7]
])
b_11_22 = np.array([50, -30, 40])
x_11_22 = np.linalg.solve(A_11_22, b_11_22)
print(f"Solusi {x_11_22}")
print(f"Transpose A:\n{A_11_22.T}")
print(f"Inverse A:\n{np.round(np.linalg.inv(A_11_22), 4)}")