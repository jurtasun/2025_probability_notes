import numpy as np
import matplotlib.pyplot as plt

# Style settings
figsize = (6, 4)
bar_color = "skyblue"
line_color = "crimson"
edgecolor = 'black'
alpha = 0.7

# Function to plot and save a histogram with mean and std lines (no title)
def plot_distribution(data, filename):
    mean_val = np.mean(data)
    std_val = np.std(data)
    
    bins = 'auto' if len(np.unique(data)) > 10 else range(min(data), max(data)+2)
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.hist(data, bins=bins, color=bar_color, edgecolor=edgecolor, alpha=alpha)
    
    # Mean line
    ax.axvline(mean_val, color=line_color, linestyle='-', linewidth=2.0, label=f'Mean = {mean_val:.2f}')
    # ±1 SD lines
    ax.axvline(mean_val - std_val, color=line_color, linestyle='--', linewidth=1.5, label=f'-1 SD = {mean_val - std_val:.2f}')
    ax.axvline(mean_val + std_val, color=line_color, linestyle='--', linewidth=1.5, label=f'+1 SD = {mean_val + std_val:.2f}')
    
    ax.set_xlabel("Observation")
    ax.set_ylabel("Frequency")
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 📌 1. Poisson Distribution
poisson_data = np.random.poisson(lam=5, size=1000)
plot_distribution(poisson_data, "poisson_hist.png")

# 📌 2. Uniform (Flat) Distribution
uniform_data = np.random.uniform(low=0, high=10, size=1000)
plot_distribution(uniform_data, "uniform_hist.png")

# 📌 3. Gaussian (Normal) Distribution
normal_data = np.random.normal(loc=5, scale=2, size=1000)
plot_distribution(normal_data, "normal_hist.png")
