# NAMA: Muhammad Rafly Wahyudi
# NPM: 24083010078

import numpy as np
import matplotlib.pyplot as plt

# Interval
x = np.linspace(0, 10, 500)
dx = x[1] - x[0]  # Lebar interval

# Deret fungsi sinusoidal
f = np.sin(x) + 0.5*np.sin(2*x) + (1/3)*np.sin(3*x) + (1/4)*np.sin(4*x) + (1/5)*np.sin(5*x)

#DIFERENSIAL (TURUNAN)
f_prime = np.zeros_like(x)
for i in range(1, len(x)-1):
    f_prime[i] = (f[i+1] - f[i-1]) / (2*dx)

#Handle boundary points
f_prime[0] = (f[1] - f[0]) / dx
f_prime[-1] = (f[-1] - f[-2]) / dx 

#INTEGRAL (METODE RIEMANN)
F = np.zeros_like(x)
for i in range(1, len(x)):
    F[i] = F[i-1] + f[i] * dx  #Jumlah Riemann

F_positive = np.zeros_like(x)  
F_negative = np.zeros_like(x)  

for i in range(1, len(x)):
    if f[i] >= 0:
        F_positive[i] = F_positive[i-1] + f[i] * dx
        F_negative[i] = F_negative[i-1]
    else:
        F_positive[i] = F_positive[i-1]
        F_negative[i] = F_negative[i-1] + f[i] * dx

print("HASIL PERHITUNGAN INTEGRAL DAN DIFERENSIAL")
print("=" * 50)
print(f"Integral total dari 0 hingga 10: {F[-1]:.6f}")
print(f"Integral bagian positif (di atas y=0): {F_positive[-1]:.6f}")
print(f"Integral bagian negatif (di bawah y=0): {F_negative[-1]:.6f}")
print(f"Verifikasi: Positif + Negatif = {F_positive[-1] + F_negative[-1]:.6f}")


plt.figure(figsize=(12, 10))

#Plot fungsi f(x)
plt.subplot(3, 1, 1)
plt.plot(x, f, 'b-', linewidth=2, label='f(x)')
plt.fill_between(x, f, where=(f>=0), color='blue', alpha=0.2, label='Area positif')
plt.fill_between(x, f, where=(f<0), color='red', alpha=0.2, label='Area negatif')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.title('Fungsi Asli f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, alpha=0.3)

#Plot turunan f'(x)
plt.subplot(3, 1, 2)
plt.plot(x, f_prime, 'g-', linewidth=2, label="f'(x)")
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.title('Turunan Fungsi f(x)')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True, alpha=0.3)

#Plot integral F(x)
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

print("\nANALISIS HASIL:")
print("=" * 85)
print("1. Integral total bernilai positif, menunjukkan area di atas sumbu x lebih dominan")
print("2. Fungsi memiliki osilasi kompleks dengan multiple frekuensi")
print("3. Turunan menunjukkan perubahan laju yang cepat sesuai osilasi fungsi")
print("4. Integral menunjukkan akumulasi area yang bervariasi sepanjang interval")