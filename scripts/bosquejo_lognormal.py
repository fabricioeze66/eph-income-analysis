# Bosquejo de distribuciones hipotéticas de ingreso (log-normal)
# Compara media vs. mediana bajo asimetría positiva: Gran Santa Fe y CABA.
# Autor: Fabricio Vera — Métodos Estadísticos para las Ciencias Sociales, FHUC-UNL

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 5, 500)

# Curva GSF
media_gsf = 0.4
sigma_gsf = 0.6
curva_gsf = (1 / (x * sigma_gsf * np.sqrt(2 * np.pi))) * np.exp(-((np.log(x) - media_gsf)**2) / (2 * sigma_gsf**2))

# Curva CABA
media_caba = 0.9
sigma_caba = 0.7
curva_caba = (1 / (x * sigma_caba * np.sqrt(2 * np.pi))) * np.exp(-((np.log(x) - media_caba)**2) / (2 * sigma_caba**2))

# Mediana y media de cada distribución (fórmulas de la log-normal)
mediana_gsf = np.exp(media_gsf)
media_real_gsf = np.exp(media_gsf + sigma_gsf**2 / 2)
mediana_caba = np.exp(media_caba)
media_real_caba = np.exp(media_caba + sigma_caba**2 / 2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# ── Subgráfico GSF ──
ax1.plot(x, curva_gsf, color='blue', linewidth=2)
ax1.fill_between(x, curva_gsf, alpha=0.15, color='blue')
ax1.axvline(mediana_gsf, color='blue', linestyle='--', linewidth=1.5, label='Mediana')
ax1.axvline(media_real_gsf, color='red', linestyle='--', linewidth=1.5, label='Media')
ax1.set_title("Gran Santa Fe (hipotético)", fontsize=11)
ax1.set_xlabel("Ingreso relativo")
ax1.set_ylabel("Densidad")
ax1.legend()

# ── Subgráfico CABA ──
ax2.plot(x, curva_caba, color='orange', linewidth=2)
ax2.fill_between(x, curva_caba, alpha=0.15, color='orange')
ax2.axvline(mediana_caba, color='orange', linestyle='--', linewidth=1.5, label='Mediana')
ax2.axvline(media_real_caba, color='red', linestyle='--', linewidth=1.5, label='Media')
ax2.set_title("CABA (hipotético)", fontsize=11)
ax2.set_xlabel("Ingreso relativo")
ax2.legend()

ax1.text(2.5, 0.45, "Media > Mediana\n(asimetría +)", fontsize=9, color='gray', ha='center')
ax2.text(4.0, 0.25, "Media > Mediana\n(asimetría +)", fontsize=9, color='gray', ha='center')

plt.suptitle("Bosquejo 1. Distribuciones hipotéticas de ingreso", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("bosquejo_lognormal.png", dpi=150)
print("Listo!")
