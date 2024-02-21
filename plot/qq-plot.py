import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns



# Generate random samples from the first distribution
# sample1 = np.random.normal(loc=0, scale=1, size=1000)  # Replace with your own data

# Generate random samples from the second distribution
# sample2 = np.random.normal(loc=0, scale=1, size=1000)  # Replace with your own data


data = pd.read_excel("cmr_errors.xlsx")  # , sheet_name="Sheet1"

print(data.keys())
# 'Iteration0', 'Errors_t', 'Errors_r', 'cmrIteration1', 'Errors_t.1',
#        'Errors_r.1', 'Iteration1', 'Errors_t.2', 'Errors_r.2'


sample1 = data['Errors_t.1'].values
sample2 = data['Errors_t.2'].values

# sample1 = data['Errors_r.1'].values
# sample2 = data['Errors_r.2'].values


# Sort the samples in ascending order
sample1_sorted = np.sort(sample1)
sample2_sorted = np.sort(sample2)

# Calculate the quantiles for each sample
quantiles = np.arange(0.01, 1, 0.001)
quantile_values_sample1 = np.percentile(sample1_sorted, quantiles * 100)
quantile_values_sample2 = np.percentile(sample2_sorted, quantiles * 100)

# print("quantile_values_sample1:", quantile_values_sample1)

# quantile_values_sample1 = (quantile_values_sample1 - np.min(quantile_values_sample1)) / (np.max(quantile_values_sample1) - np.min(quantile_values_sample1)) * 100
# quantile_values_sample2 = (quantile_values_sample2 - np.min(quantile_values_sample2)) / (np.max(quantile_values_sample2) - np.min(quantile_values_sample2)) * 100



# Plot the QQ plot
# Set up the plot style
sns.set(style="whitegrid", font_scale=1.2)

# Plot the QQ plot
plt.figure(figsize=(8, 6))
plt.plot(quantile_values_sample1, quantile_values_sample2, 'o', markersize=6, color='steelblue')
plt.plot([np.min(quantile_values_sample1), np.max(quantile_values_sample1)],
         [np.min(quantile_values_sample1), np.max(quantile_values_sample1)], 'r--', linewidth=1.5)

plt.xlabel('Quantiles of Sample 1', fontsize=14)
plt.ylabel('Quantiles of Sample 2', fontsize=14)
plt.title('Quantile-Quantile Plot', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("qq-plot2.png")
plt.show()