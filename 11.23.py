# Rut Naomi E.S || F55123057
# Untuk soal 11.23: Perbandingan jumlah operasi antara Thomas Algorithm dan Gauss
import numpy as np
import matplotlib.pyplot as plt

# Soal 11.23: Jumlah operasi Thomas vs Gauss Elimination
# Gauss Elimination (tanpa partial pivoting) membutuhkan sekitar (2 * n^3) / 3 operasi.
# Thomas Algorithm untuk matriks tridiagonal hanya membutuhkan sekitar 8n operasi.

n = np.arange(2, 21)
ops_gauss = (2/3) * (n**3)
ops_thomas = 8 * n

# Menampilkan sedikit perbandingan angkanya
print("=== Soal 11.23: Operasi Komputasi ===")
print("n\t| Gauss\t\t| Thomas")
print("-" * 35)
for i in range(0, len(n), 2):
    print(f"{n[i]}\t| {ops_gauss[i]:.1f}\t\t| {ops_thomas[i]:.1f}")

# Jika dijalankan di environment lokal, aktifkan plot di bawah ini:
'''
plt.figure(figsize=(8, 5))
plt.plot(n, ops_gauss, label='Gauss Elimination $O(n^3)$', marker='o')
plt.plot(n, ops_thomas, label='Thomas Algorithm $O(n)$', marker='s')
plt.title('Jumlah Operasi: Thomas Algorithm vs Gauss Elimination')
plt.xlabel('Ukuran Matriks (n)')
plt.ylabel('Jumlah Operasi')
plt.legend()
plt.grid(True)
plt.show()
'''