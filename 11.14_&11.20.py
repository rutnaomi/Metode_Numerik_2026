# Rut Naomi E.S || F55123057
# Untuk soal 11.14 dan 11.20

import numpy as np
import matplotlib.pyplot as plt

print("=== Soal 11.14: Gauss-Seidel pada Slope 1 dan 1 ===")
print("Jika dua persamaan memiliki slope (kemiringan) 1 dan 1, ini berarti")
print("kedua garis tersebut sejajar (tidak ada solusi) atau berimpit (solusi tak hingga).")
print("Sistem ini bersifat singular (determinannya 0).")
print("Menerapkan Gauss-Seidel pada sistem ini akan menyebabkan pembagian dengan nol")
print("atau nilai yang terus membesar (divergen), sehingga metode ini GAGAL.\n")

print("=== Soal 11.20: Matriks Vandermonde 6-Dimensi ===")
# Nilai x yang diberikan
x_vals = np.array([4, 2, 7, 10, 3, 5])

# Membuat Matriks Vandermonde secara berurutan
# v_{i,j} = x_i^{j-1}
V_6 = np.vander(x_vals, increasing=True)
print("Matriks Vandermonde [V]:")
print(V_6)

# Ruas kanan {b} adalah jumlah dari koefisien di barisnya masing-masing
b_11_20 = np.sum(V_6, axis=1)

# Condition number (Spectral)
cond_vander = np.linalg.cond(V_6, p=2)
print(f"\nSpectral Condition Number: {cond_vander:.5e}")
print(f"Perkiraan digit presisi yang hilang: {np.log10(cond_vander):.2f} digit.")

# Penyelesaian sistem V * x = b
x_11_20 = np.linalg.solve(V_6, b_11_20)
x_true = np.ones(6) # Karena b adalah jumlah baris, x seharusnya adalah vektor angka 1

# Menghitung Error
error = np.abs((x_true - x_11_20) / x_true) * 100
print(f"Solusi x terhitung: {np.round(x_11_20, 6)}")
print(f"Persentase Error dari x eksak (1.0): {np.max(error):.4e} %")
print("Kesimpulan: Matriks Vandermonde seringkali ill-conditioned, namun pada kasus ini")
print("Python masih dapat menanganinya dengan baik (error mendekati nol).")