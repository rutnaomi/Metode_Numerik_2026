# Rut Naomi E.S || F55123057
# Untuk soal 11.2: Invers Matriks menggunakan Dekomposisi LU

import numpy as np
import scipy.linalg as la

def inverse_via_lu(A):
    """
    Menghitung invers matriks menggunakan dekomposisi LU
    dan penyelesaian vektor satuan secara berurutan.
    """
    n = A.shape[0]
    A_inv = np.zeros((n, n))
    
    # dekomposisi LU menggunakan scipy
    P, L, U = la.lu(A)
    
    # matriks identitas (kumpulan vektor satuan)
    I = np.eye(n)
    
    for i in range(n):
        # ambil vektor satuan ke-i
        e_i = I[:, i]
        
        # selesaikan L * y = P * e_i (Forward substitution)
        # note: SciPy mengembalikan A = P * L * U, 
        # sehingga persamaannya jadi L * U * x = P^T * e_i
        y = la.solve_triangular(L, np.dot(P.T, e_i), lower=True)
        
        # selesaikan U * x = y (Backward substitution)
        x = la.solve_triangular(U, y, lower=False)
        
        # simpan vektor solusi sebagai kolom ke-i di matriks invers
        A_inv[:, i] = x
        
    return A_inv

print("=== Hasil Soal 11.2 ===")
# menggunakan matriks tridiagonal dari soal 11.1 sebagai referensi
A_matrix = np.array([
    [0.8, -0.4,  0.0],
    [-0.4,  0.8, -0.4],
    [0.0, -0.4,  0.8]
])

inverse_A = inverse_via_lu(A_matrix)

print("Matriks A:")
print(A_matrix)
print("\nInvers dari A berdasarkan Dekomposisi LU:")
print(inverse_A)

# verifikasi: A * A_inv harus menghasilkan matriks Identitas
print("\nVerifikasi (A * A_inv):")
print(np.round(np.dot(A_matrix, inverse_A), decimals=5))