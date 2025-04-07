# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm, uniform, expon

# Define the figure size and color
figsize = (6, 4)
color = "#1f77b4"  # Nice blue color

# Bernoulli Distribution
p = 0.5
x_bernoulli = [0, 1]
y_bernoulli = [1 - p, p]
plt.figure(figsize=figsize)
plt.bar(x_bernoulli, y_bernoulli, color=color, edgecolor='black', linewidth=1.0, alpha=0.7)
plt.xlabel("x")
plt.ylabel("p(x)")
plt.xticks([0, 1])
plt.savefig("bernoulli.png")
plt.close()

# Binomial Distribution
fig, ax = plt.subplots(figsize=figsize)
n, p = 20, 0.5
x_binom = np.arange(0, n+1)
y_binom = binom.pmf(x_binom, n, p)
ax.bar(x_binom, y_binom, color=color, edgecolor='black', linewidth=1.0, alpha=0.7)
ax.set_xlabel("x")
ax.set_ylabel("p(x)")
plt.savefig("binomial.png")
plt.close()

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

# Gaussian (Normal) Distribution
fig, ax = plt.subplots(figsize=figsize)
mu, sigma = 0, 1
x_norm = np.linspace(-4, 4, 1000)
y_norm = norm.pdf(x_norm, mu, sigma)
ax.plot(x_norm, y_norm, color=color)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.savefig("normal.png")
plt.close()

# Uniform Distribution
fig, ax = plt.subplots(figsize=figsize)
x_uniform = np.linspace(-1, 2, 1000)
y_uniform = uniform.pdf(x_uniform, 0, 1)
ax.plot(x_uniform, y_uniform, color=color)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.savefig("uniform.png")
plt.close()

# Exponential Distribution
fig, ax = plt.subplots(figsize=figsize)
lambda_exp = 1
x_expon = np.linspace(0, 5, 1000)
y_expon = expon.pdf(x_expon, scale=1/lambda_exp)
ax.plot(x_expon, y_expon, color=color)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.savefig("exponential.png")
plt.close()