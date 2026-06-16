# Rut Naomi E.S || F55123057
# Untuk soal 11.1, 11.3: Penyelesaian sistem tridiagonal menggunakan Algoritma Thomas
import numpy as np

def thomas_algorithm(a, b, c, d):
    """
    Penyelesaian sistem tridiagonal menggunakan Algoritma Thomas.
    a: sub-diagonal (bawah), panjang n-1
    b: diagonal utama, panjang n
    c: super-diagonal (atas), panjang n-1
    d: vektor hasil (ruas kanan), panjang n
    """
    n = len(d)
    c_star = np.zeros(n-1)
    d_star = np.zeros(n)
    x = np.zeros(n)

    # Forward elimination
    c_star[0] = c[0] / b[0]
    d_star[0] = d[0] / b[0]
    
    for i in range(1, n-1):
        c_star[i] = c[i] / (b[i] - a[i-1] * c_star[i-1])
    
    for i in range(1, n):
        d_star[i] = (d[i] - a[i-1] * d_star[i-1]) / (b[i] - a[i-1] * c_star[i-1])

    # Backward substitution
    x[-1] = d_star[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_star[i] - c_star[i] * x[i+1]
        
    return x

# eksekusi untuk SOAL 11.1
print("=== Hasil Soal 11.1 ===")
# Diagonal utama (b), sub-diagonal (a), super-diagonal (c), ruas kanan (d)
b_11_1 = np.array([0.8, 0.8, 0.8])
a_11_1 = np.array([-0.4, -0.4])
c_11_1 = np.array([-0.4, -0.4])
d_11_1 = np.array([41.0, 25.0, 105.0])

x_11_1 = thomas_algorithm(a_11_1, b_11_1, c_11_1, d_11_1)
print(f"Solusi x untuk 11.1: {x_11_1}\n")

# eksekusi untuk SOAL 11.3

print("=== Hasil Soal 11.3 ===")
b_11_3 = np.array([2.01475, 2.01475, 2.01475, 2.01475])
a_11_3 = np.array([-0.020875, -0.020875, -0.020875])
c_11_3 = np.array([-0.020875, -0.020875, -0.020875])
d_11_3 = np.array([4.175, 0.0, 0.0, 2.0875])

x_11_3 = thomas_algorithm(a_11_3, b_11_3, c_11_3, d_11_3)
print(f"Solusi T untuk 11.3: {x_11_3}")