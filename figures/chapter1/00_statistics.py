# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# Plot styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

# Colors
main_color = "#1f77b4"
highlight_color = 'firebrick'

# Common formatting function
def format_axes(ax):
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='both', direction='in', length=4, width=1)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)


# =============================
# 1. Binomial Distribution
# =============================
n, p = 10, 0.5
samples_binom = np.random.binomial(n, p, size=10000)
x_vals = np.arange(0, n + 1)
pmf_vals = binom.pmf(x_vals, n, p)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(samples_binom, bins=np.arange(-0.5, n + 1.5, 1),
        density=True, color=main_color, alpha=0.6,
        edgecolor="black", linewidth=1.0, label="Samples")
ax.plot(x_vals, pmf_vals, 'o-', color=highlight_color, lw=2, label="PMF")

ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel("Probability", fontsize=14)
ax.set_xlim(-0.5, n + 0.5)
ax.set_ylim(0, 0.3)
ax.legend()
format_axes(ax)

plt.tight_layout()
fig.savefig("sampling_binomial.png", dpi=300, bbox_inches='tight')
fig.savefig("sampling_binomial.pdf", bbox_inches='tight')
plt.show()


# =============================
# 2. Poisson Distribution
# =============================
lam = 4
samples_pois = np.random.poisson(lam, size=10000)
x_vals = np.arange(0, 15)
pmf_vals = poisson.pmf(x_vals, lam)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(samples_pois, bins=np.arange(-0.5, 15.5, 1),
        density=True, color=main_color, alpha=0.6,
        edgecolor="black", linewidth=1.0, label="Samples")
ax.plot(x_vals, pmf_vals, 'o-', color=highlight_color, lw=2, label="PMF")

ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel("Probability", fontsize=14)
ax.set_xlim(-0.5, 15)
ax.set_ylim(0, 0.25)
ax.legend()
format_axes(ax)

plt.tight_layout()
fig.savefig("sampling_poisson.png", dpi=300, bbox_inches='tight')
fig.savefig("sampling_poisson.pdf", bbox_inches='tight')
plt.show()


# =============================
# 3. Normal Distribution
# =============================
mu, sigma = 0, 1
samples_norm = np.random.normal(mu, sigma, size=10000)
x_vals = np.linspace(-4, 4, 200)
pdf_vals = norm.pdf(x_vals, mu, sigma)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(samples_norm, bins=30, density=True,
        color=main_color, alpha=0.6,
        edgecolor="black", linewidth=1.0, label="Samples")
ax.plot(x_vals, pdf_vals, '-', color=highlight_color, lw=2, label="PDF")

ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel("Density", fontsize=14)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.45)
ax.legend()
format_axes(ax)

plt.tight_layout()
fig.savefig("sampling_normal.png", dpi=300, bbox_inches='tight')
fig.savefig("sampling_normal.pdf", bbox_inches='tight')
plt.show()
