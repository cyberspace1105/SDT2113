import numpy as np
import matplotlib.pyplot as plt

np.random.seed(58)

# Simulate rolling a fair six-sided die
num_rolls = 200000

rolls = np.random.randint(1, 7, size=num_rolls)
print(rolls)

# Calculate the probability mass function (PMF)
pmf, bins = np.histogram(rolls, bins=np.arange(1, 8), density=True)

# Calculate the cumulative distribution function (CDF)
cdf = np.cumsum(pmf)

# Calculate the mean, variance, and standard deviation
mean = np.mean(rolls)
variance = np.var(rolls)
std_deviation = np.std(rolls)

# Print the mean, variance, and standard deviation
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# Plot the PMF using stem plot
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, subplot 1
plt.stem(bins[:-1], pmf, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('Outcome x')
plt.ylabel('Probability')
plt.title('PMF of rolling a dice')

# Plot the CDF
plt.subplot(1, 2, 2)  # 1 row, 2 columns, subplot 2
plt.plot(bins[:-1], cdf, marker='o', linestyle='-', color='red')
plt.xlabel('Outcome x')
plt.ylabel('Cumulative Probability')
plt.title('CDF of rolling a dice')

# Show plots
plt.tight_layout()
plt.show()
