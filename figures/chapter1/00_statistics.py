# Import libraries
import numpy as np
import matplotlib.pyplot as plt

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
extra_color = "#2ca02c"

colors = [main_color, highlight_color, extra_color]

# Common formatting function
def format_axes(ax):
    ax.grid(True, linestyle='--', alpha=0.1)
    ax.tick_params(axis='both', direction='in', length=4, width=1)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)

# =============================
# Measurements Visualization
# =============================

# Generate three small sets of measurements
np.random.seed(42)
measurements1 = np.random.normal(loc=45, scale=2, size=30)
measurements2 = np.random.normal(loc=50, scale=2, size=25)
measurements3 = np.random.normal(loc=55, scale=3, size=20)

groups = [measurements1, measurements2, measurements3]
labels = ["Set 1", "Set 2", "Set 3"]

# 1. Histogram (overlayed)
fig, ax = plt.subplots(figsize=(7, 4.5))
bins = np.linspace(40, 60, 15)
for data, c, lab in zip(groups, colors, labels):
    ax.hist(data, bins=bins, alpha=0.6, color=c, edgecolor="black", linewidth=1.0, label=lab)

ax.set_xlabel("Measurement value", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)
ax.legend()
format_axes(ax)

plt.tight_layout()
fig.savefig("measurements_histogram.png", dpi=300, bbox_inches='tight')
fig.savefig("measurements_histogram.pdf", bbox_inches='tight')
plt.show()

# 2. Box plot
fig, ax = plt.subplots(figsize=(7, 4.5))
box = ax.boxplot(groups, patch_artist=True, labels=labels,
                 boxprops=dict(color="black"),
                 medianprops=dict(color="black", linewidth=2),
                 whiskerprops=dict(color="black"),
                 capprops=dict(color="black"),
                 flierprops=dict(marker='o', markersize=5, linestyle="none", alpha=0.7))

# Color each box
for patch, c in zip(box['boxes'], colors):
    patch.set_facecolor(c)
    patch.set_alpha(0.6)
for med in box['medians']:
    med.set_color(highlight_color)
    med.set_linewidth(2)

ax.set_ylabel("Value", fontsize=14)
format_axes(ax)

plt.tight_layout()
fig.savefig("measurements_boxplot.png", dpi=300, bbox_inches='tight')
fig.savefig("measurements_boxplot.pdf", bbox_inches='tight')
plt.show()

# 3. Violin plot
fig, ax = plt.subplots(figsize=(7, 4.5))
parts = ax.violinplot(groups, showmedians=True, showextrema=True)

# Style violins
for pc, c in zip(parts['bodies'], colors):
    pc.set_facecolor(c)
    pc.set_edgecolor("black")
    pc.set_alpha(0.6)
parts['cmedians'].set_color("black")
parts['cmedians'].set_linewidth(2)
for partname in ('cbars','cmins','cmaxes'):
    vp = parts[partname]
    vp.set_edgecolor("black")
    vp.set_linewidth(1)

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(labels, fontsize=13)
ax.set_ylabel("Value", fontsize=14)
format_axes(ax)

plt.tight_layout()
fig.savefig("measurements_violin.png", dpi=300, bbox_inches='tight')
fig.savefig("measurements_violin.pdf", bbox_inches='tight')
plt.show()
