import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a DataFrame
df = pd.read_csv("q_03.csv")

# Get unique standard quartiles and categories and sort categories alphabetically
standard_quartiles = sorted(df['standard_quartile'].unique())
categories = df['category_name'].unique()

# Create a dictionary to store movie counts for each standard quartile and category
data_dict = {standard_quartile: [] for standard_quartile in standard_quartiles}

# Group the data by standard quartile and category
for standard_quartile in standard_quartiles:
    for category in categories:
        subset = df[(df['standard_quartile'] == standard_quartile) & (df['category_name'] == category)]
        data_dict[standard_quartile].append(subset['count'].sum())

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Define the width of each bar and the positions for each group
width = 0.15
x = np.arange(len(categories))

# Create bars for each standard quartile
for i, standard_quartile in enumerate(standard_quartiles):
    bars = ax.bar(x + i * width, data_dict[standard_quartile], width=width, label=f'Q{standard_quartile}')
    
    # Add text labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset for the label
                    textcoords="offset points",
                    ha='center', va='bottom')

# Customize the plot
ax.set_xlabel("Category", fontsize=10, fontweight='bold')
ax.set_ylabel("Number of Movies", fontsize=10, fontweight='bold')
ax.set_title("Movie Distribution by Category for Each Quartile", fontsize=12, fontweight='bold')
ax.set_xticks(x + width * (len(standard_quartiles) - 1) / 2)
ax.set_xticklabels(categories)
ax.legend(title="Standard Quartile")

# Show the grouped bar chart
plt.tight_layout()
plt.show()
