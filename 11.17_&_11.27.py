# Rut Naomi E.S || F55123057
# Untuk soal 11.17 dan 11.27

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

print("=== Soal 11.17: Persamaan Non-Linear ===")
def equations(vars):
    x, y = vars
    eq1 = 4 - y - 2 * x**2
    eq2 = 8 - y**2 - 4 * x
    return [eq1, eq2]

# Mencoba berbagai tebakan awal (initial guesses)
guesses = [(1, 1), (-3, -3), (3, -3)]
for i, guess in enumerate(guesses):
    sol = fsolve(equations, guess)
    print(f"Tebakan awal {guess} menghasilkan solusi: x = {sol[0]:.4f}, y = {sol[1]:.4f}")

print("\n=== Soal 11.27: BVP dengan Finite Difference ===")
# Parameter: D=2, U=1, k=0.2, c(0)=80, c(10)=20, dx=2
# Persamaan diskrit di node internal i:
# (D/dx^2 + U/2dx) c_{i-1} - (2D/dx^2 + k) c_i + (D/dx^2 - U/2dx) c_{i+1} = 0
D = 2.0; U = 1.0; k = 0.2; dx = 2.0
alpha = D / (dx**2)    # 0.5
beta = U / (2 * dx)    # 0.25

# Koefisien
c_min_1 = alpha + beta   # 0.75
c_i = -(2 * alpha + k)   # -1.2
c_plus_1 = alpha - beta  # 0.25

# Matriks Tridiagonal untuk 4 node internal (x=2, 4, 6, 8)
A_11_27 = np.array([
    [c_i, c_plus_1, 0, 0],
    [c_min_1, c_i, c_plus_1, 0],
    [0, c_min_1, c_i, c_plus_1],
    [0, 0, c_min_1, c_i]
])

# Ruas kanan (memasukkan kondisi batas c(0)=80 dan c(10)=20)
b_11_27 = np.array([-c_min_1 * 80.0, 0, 0, -c_plus_1 * 20.0])

c_internal = np.linalg.solve(A_11_27, b_11_27)
jarak = [0, 2, 4, 6, 8, 10]
konsentrasi = [80] + list(c_internal) + [20]

print(f"Jarak x: {jarak}")
print(f"Konsentrasi C: {[round(c, 2) for c in konsentrasi]}")
