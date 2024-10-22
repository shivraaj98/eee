import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set styles for better visualization
plt.rc("font", size=14)
sns.set(style="whitegrid", color_codes=True)

# Load the dataset
data = pd.read_csv('bank.csv')

# Create a bar plot for purchase frequency by job title
pd.crosstab(data['job'], data['y']).plot(kind='bar', figsize=(10, 6))

# Customize the plot
plt.title('Purchase Frequency by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Frequency of Purchase')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a file
plt.savefig('purchase_frequency_by_job.png')

# Display the plot
plt.show()
