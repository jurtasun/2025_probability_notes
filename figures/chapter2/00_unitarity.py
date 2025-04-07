# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm, uniform, expon

# Define the figure size and color
figsize = (6, 4)
color = "#1f77b4"  # Nice blue color
highlight_color = 'red'

# Poisson Distribution
fig, ax = plt.subplots(figsize=figsize)
lambda_ = 5
x_poisson = np.arange(0, 20)
y_poisson = poisson.pmf(x_poisson, lambda_)
ax.bar(x_poisson, y_poisson, color=color, edgecolor='black', linewidth=1.0, alpha=0.7)
ax.set_xlabel("x")
ax.set_ylabel("p(x)")
plt.savefig("poisson.png")
plt.close()

# Poisson Distribution
lambda_ = 5
x_poisson = np.arange(0, 20)
y_poisson = poisson.pmf(x_poisson, lambda_)

# Bar colors: red for x >= 5
bar_colors = [highlight_color if x >= 5 else color for x in x_poisson]

plt.figure(figsize=figsize)
plt.bar(x_poisson, y_poisson, color=bar_colors, edgecolor='black', linewidth=1.0, alpha=0.7)
plt.axvline(x=5, color='black', linestyle='--', linewidth=1.2)
plt.xlabel("x")
plt.ylabel("p(x)")
plt.savefig("poisson_highlight.png")
plt.close()