
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

# Perform T-Test analysis between 'Age' and 'Grip strength'
ttest_results = ttest_ind(df_filtered['Age'], df_filtered['Grip strength'])

# Display T-Test results in tabular form
ttest_table = pd.DataFrame({
    'Statistic': [ttest_results.statistic],
    'P-value': [ttest_results.pvalue]
})

print("T-Test Results for Age and Grip Strength:")
print(ttest_table)

# Plotting a Hexbin plot: Age vs Grip Strength with color intensity
plt.figure(figsize=(8, 6))
hb = plt.hexbin(df_filtered['Age'], df_filtered['Grip strength'], gridsize=30, cmap='Blues')

# Adding a color bar to indicate density
cb = plt.colorbar(hb)
cb.set_label('Counts')

# Customize plot
plt.xlabel('Age')
plt.ylabel('Grip Strength')
plt.title('Hexbin Plot: Age vs Grip Strength')
plt.grid(True)

# Display the plot
plt.show()
