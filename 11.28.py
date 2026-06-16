# Rut Naomi E.S || F55123057
# untuk soal terakhir 11.28

import numpy as np

def solve_pentadiagonal(e, a, d, c, f, b):
    """
    Penyelesaian sistem pentadiagonal.
    e: sub-sub-diagonal (panjang n-2)
    a: sub-diagonal (panjang n-1)
    d: diagonal utama (panjang n)
    c: super-diagonal (panjang n-1)
    f: super-super-diagonal (panjang n-2)
    b: vektor ruas kanan (panjang n)
    """
    n = len(d)
    x = np.zeros(n)
    
    # Buat salinan agar array asli tidak berubah
    d_ = d.copy()
    c_ = c.copy()
    f_ = np.pad(f, (0, 2), mode='constant') # Pad f agar seragam
    b_ = b.copy()
    a_ = np.pad(a, (1, 0), mode='constant') # Pad a
    e_ = np.pad(e, (2, 0), mode='constant') # Pad e

    # Forward Elimination
    for i in range(n - 1):
        if i > 0:
            mult_a = a_[i] / d_[i-1]
            d_[i] = d_[i] - mult_a * c_[i-1]
            c_[i] = c_[i] - mult_a * f_[i-1]
            b_[i] = b_[i] - mult_a * b_[i-1]
            
        mult_e = e_[i+1] / d_[i] if i < n-2 else 0
        if mult_e != 0:
            a_[i+1] = a_[i+1] - mult_e * c_[i]
            d_[i+1] = d_[i+1] - mult_e * f_[i]
            b_[i+1] = b_[i+1] - mult_e * b_[i]

    mult_a = a_[-1] / d_[-2]
    d_[-1] = d_[-1] - mult_a * c_[-1]
    b_[-1] = b_[-1] - mult_a * b_[-2]

    # Backward Substitution
    x[-1] = b_[-1] / d_[-1]
    x[-2] = (b_[-2] - c_[-1] * x[-1]) / d_[-2]
    
    for i in range(n - 3, -1, -1):
        x[i] = (b_[i] - c_[i] * x[i+1] - f_[i] * x[i+2]) / d_[i]

    return x

print("=== Soal 11.28: Algoritma Pentadiagonal ===")
# Mendefinisikan matriks dari soal 11.28
d = np.array([ 8.0,  9.0,  7.0, 12.0, 15.0])
a = np.array([-2.0, -3.0, -2.0, -3.0])
c = np.array([-2.0, -4.0, -1.0, -5.0])
e = np.array([-1.0, -4.0, -7.0])
f = np.array([-1.0, -1.0, -2.0])
b = np.array([ 5.0,  2.0,  1.0,  1.0,  5.0])

x_11_28 = solve_pentadiagonal(e, a, d, c, f, b)
print(f"Solusi x untuk sistem pentadiagonal:\n{np.round(x_11_28, 4)}")