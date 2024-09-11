import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Set seed for reproducibility
np.random.seed(42)

# Parameters of the exponential distribution
lambda_param = 0.5  # Rate parameter

# Number of random variates to generate
sample_size = 1000

# Generate uniform (0,1) variates
uniform_variates = np.random.rand(sample_size)

# Calculate the inverse of the exponential CDF
def inverse_exponential_cdf(u, lambda_param):
    return -np.log(1 - u) / lambda_param  

# Transform uniform variates using the inverse CDF
exponential_variates = inverse_exponential_cdf(uniform_variates, lambda_param)

# Plot the histogram of generated variates
plt.hist(exponential_variates, bins=50, density=True, alpha=0.6, color='lightgreen', label='Generated Exponential Variates')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram of Exponential Distribution')
plt.legend()
plt.show()


# Transform uniform variates using the inverse CDF
exponential_variates = inverse_exponential_cdf(uniform_variates, lambda_param)

# Plot the histogram of generated variates
plt.hist(exponential_variates, bins=50, density=True, alpha=0.6, color='lightgreen', label='Generated Exponential Variates')

# Plot the exponential variates using scipy 
x = np.linspace(0, 10, 1000)
theoretical_pdf = expon.pdf(x, scale=1/lambda_param)
plt.plot(x, theoretical_pdf, 'r--', label=' Exponential (SciPy)')

plt.xlabel('Value')
plt.ylabel('Probability Density')

plt.title('Generated Exponential Variates vs Exponential (SciPy)')
plt.legend()

plt.grid(True)
plt.show()
