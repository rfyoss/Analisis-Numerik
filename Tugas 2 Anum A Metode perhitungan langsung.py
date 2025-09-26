# NAMA: Muhammad Rafly Wahyudi
# NPM: 24083010078

import numpy as np
import matplotlib.pyplot as plt

def turunan(x, f):
    n = len(x)
    f_prime = np.zeros(n)
    dx = x[1] - x[0]
    
    for i in range(1, n-1):
        f_prime[i] = (f[i+1] - f[i-1]) / (2 * dx)
    
    f_prime[0] = (f[1] - f[0]) / dx
    f_prime[-1] = (f[-1] - f[-2]) / dx
    
    return f_prime

def integral(x, f):
    n = len(x)
    F = np.zeros(n)
    dx = x[1] - x[0]
    
    for i in range(1, n):
        F[i] = F[i-1] + f[i] * dx
    
    return F

def integral_terpisah(x, f):
    n = len(x)
    F_pos = np.zeros(n)
    F_neg = np.zeros(n)
    dx = x[1] - x[0]
    
    for i in range(1, n):
        if f[i] >= 0:
            F_pos[i] = F_pos[i-1] + f[i] * dx
            F_neg[i] = F_neg[i-1]
        else:
            F_pos[i] = F_pos[i-1]
            F_neg[i] = F_neg[i-1] + f[i] * dx
    
    return F_pos, F_neg

x = np.linspace(0, 10, 500)

f = np.sin(x) + 0.5*np.sin(2*x) + (1/3)*np.sin(3*x) + (1/4)*np.sin(4*x) + (1/5)*np.sin(5*x)

f_prime = turunan(x, f)
F_integral = integral(x, f)
F_pos, F_neg = integral_terpisah(x, f)

print("HASIL PERHITUNGAN")
print("=" * 50)
print(f"Integral total: {F_integral[-1]:.6f}")
print(f"Integral bagian positif: {F_pos[-1]:.6f}")
print(f"Integral bagian negatif: {F_neg[-1]:.6f}")
print(f"Verifikasi: {F_pos[-1] + F_neg[-1]:.6f}")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

ax1.plot(x, f, 'b-', linewidth=2, label='f(x)')
for i in range(len(x)-1):
    if f[i] >= 0:
        ax1.fill_between([x[i], x[i+1]], [f[i], f[i+1]], 0, color='blue', alpha=0.2)
for i in range(len(x)-1):
    if f[i] < 0:
        ax1.fill_between([x[i], x[i+1]], [f[i], f[i+1]], 0, color='red', alpha=0.2)
ax1.axhline(0, color='black', linestyle='--', linewidth=0.5)
ax1.set_title('Fungsi Asli f(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.grid(True, alpha=0.3)
ax1.legend()

ax2.plot(x, f_prime, 'g-', linewidth=2, label="f'(x)")
ax2.axhline(0, color='black', linestyle='--', linewidth=0.5)
ax2.set_title('Turunan Fungsi f(x)')
ax2.set_xlabel('x')
ax2.set_ylabel("f'(x)")
ax2.grid(True, alpha=0.3)
ax2.legend()

ax3.plot(x, F_integral, 'm-', linewidth=2, label='Integral total F(x)')
ax3.plot(x, F_pos, 'r--', linewidth=1.5, label='Integral bagian positif')
ax3.plot(x, F_neg, 'b--', linewidth=1.5, label='Integral bagian negatif')
ax3.axhline(0, color='black', linestyle='--', linewidth=0.5)
ax3.set_title('Integral Fungsi f(x)')
ax3.set_xlabel('x')
ax3.set_ylabel('F(x)')
ax3.grid(True, alpha=0.3)
ax3.legend()

plt.tight_layout()
plt.show()