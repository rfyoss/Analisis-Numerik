import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

x = np.linspace(3, 10, 500)
y = skewnorm.pdf(x, a=6, loc=3.5, scale=1.5) * 10
np.random.seed(78)
y = y + np.random.normal(0, 0.02, size=x.shape)

hargaproduksi = 0.5 + 0.05 * x
jumlah_barang = y * 100
biaya = jumlah_barang * hargaproduksi
pendapatan = jumlah_barang * x
profit = pendapatan - biaya

plt.figure(figsize=(12, 8))

plt.plot(x, y, 'b-', linewidth=2, label='Penjualan (ratusan)')
plt.plot(x, hargaproduksi, 'r--', linewidth=2, label='Harga Produksi per Unit')
plt.plot(x, biaya/1000, 'g-.', linewidth=2, label='Total Biaya (ribuan)')
plt.plot(x, profit/1000, 'm:', linewidth=3, label='Profit (ribuan)')

plt.title("Analisis Penjualan, Biaya, dan Profit")
plt.xlabel("Harga Jual (ribuan)")
plt.ylabel("Nilai (ratusan/ribuan)")
plt.grid(True)
plt.legend()

harga_optimal = x[np.argmax(profit)]
profit_maksimal = np.max(profit)
plt.axvline(x=harga_optimal, color='orange', linestyle='--', alpha=0.7, 
            label=f'Harga Optimal: {harga_optimal:.2f}')

plt.legend()
plt.show()