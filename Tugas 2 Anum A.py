# NAMA: Muhammad Rafly Wahyudi
# NPM: 24083010078

import numpy as np
import matplotlib.pyplot as plt

# Interval
x = np.linspace(0, 10, 500)
dx = x[1] - x[0]

# Deret fungsi sinusoidal
f = np.sin(x) + 0.5*np.sin(2*x) + (1/3)*np.sin(3*x) + (1/4)*np.sin(4*x) + (1/5)*np.sin(5*x)

# Hitung turunan
f_prime = np.zeros_like(x)
for i in range(1, len(x)-1):
    f_prime[i] = (f[i+1] - f[i-1]) / (2*dx)

# Handle boundary points
f_prime[0] = (f[1] - f[0]) / dx
f_prime[-1] = (f[-1] - f[-2]) / dx

# Hitung integral
F = np.zeros_like(x)
for i in range(1, len(x)):
    F[i] = F[i-1] + f[i] * dx

F_positive = np.zeros_like(x)
F_negative = np.zeros_like(x)

for i in range(1, len(x)):
    if f[i] >= 0:
        F_positive[i] = F_positive[i-1] + f[i] * dx
        F_negative[i] = F_negative[i-1]
    else:
        F_positive[i] = F_positive[i-1]
        F_negative[i] = F_negative[i-1] + f[i] * dx

# Plot semua fungsi
plt.figure(figsize=(12, 10))

# Plot fungsi asli f
plt.subplot(3, 1, 1)
plt.plot(x, f, 'b-', linewidth=2, label='f(x) = sin(x) + 0.5sin(2x) + (1/3)sin(3x) + (1/4)sin(4x) + (1/5)sin(5x)')
plt.fill_between(x, f, where=(f>=0), color='blue', alpha=0.2, label='Area positif')
plt.fill_between(x, f, where=(f<0), color='red', alpha=0.2, label='Area negatif')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.title('Fungsi Asli f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot turunan f'
plt.subplot(3, 1, 2)
plt.plot(x, f_prime, 'g-', linewidth=2, label="f'(x)")
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.title('Turunan Fungsi f(x)')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True, alpha=0.3)

# Plot integral F
plt.subplot(3, 1, 3)
plt.plot(x, F, 'm-', linewidth=2, label='F(x) = Integral f(x) dx')
plt.plot(x, F_positive, 'r--', linewidth=1.5, label='Integral bagian positif')
plt.plot(x, F_negative, 'b--', linewidth=1.5, label='Integral bagian negatif')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.title('Integral Fungsi f(x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Tampilkan nilai integral total, positif, dan negatif
integral_total = F[-1]
integral_positif = F_positive[-1]
integral_negatif = F_negative[-1]

print("HASIL PERHITUNGAN:")
print(f"Integral total dari 0 hingga 10: {integral_total:.4f}")
print(f"Integral bagian positif: {integral_positif:.4f}")
print(f"Integral bagian negatif: {integral_negatif:.4f}")
print(f"Verifikasi: Positif + Negatif = {integral_positif + integral_negatif:.4f} (harus sama dengan total)")

# Untuk memverifikasi, bandingkan dengan hasil numerik
from scipy.integrate import cumtrapz
F_numeric = cumtrapz(f, x, initial=0)
print(f"\nPerbandingan dengan metode numerik (trapesium): {F_numeric[-1]:.4f}")
print(f"Selisih: {abs(integral_total - F_numeric[-1]):.6f}")

