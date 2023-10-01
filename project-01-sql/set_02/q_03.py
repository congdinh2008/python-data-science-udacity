import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a DataFrame
df = pd.read_csv("q_03.csv")

# Get unique standard quartiles and categories and sort categories alphabetically
customers = sorted(df['name'].unique())
months = df['payment_month'].unique()

# Create a dictionary to store movie counts for each standard quartile and category
data_dict = {month: [] for month in months}

# Group the data by standard quartile and category
for month in months:
    for customer in customers:
        subset = df[(df['payment_month'] == month)
                    & (df['name'] == customer)]
        data_dict[month].append(subset['lead_dif'].max())

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 6))

# Define the width of each bar and the positions for each group
width = 0.15
x = np.arange(len(customers))

# Create bars for each standard quartile
for i, month in enumerate(months):
    bars = ax.bar(
        x + i * width, data_dict[month], width=width, label=f'{month}')

    # Add text labels on the inner top of each bar vertically
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # 5 points vertical offset for the label
                    textcoords="offset points",
                    ha='center', va='bottom', rotation='vertical')

# Customize the plot
ax.set_xlabel("Customer", fontsize=10, fontweight='bold')
ax.set_ylabel("Diffrence", fontsize=10, fontweight='bold')
ax.set_title("Difference of the payment amounts in each successive month of top 10 paying customer in 2007",
             fontsize=12, fontweight='bold')
ax.set_xticks(x + width * (len(months) - 1) / 2)
ax.set_xticklabels(customers)
ax.legend(title="Months")

# Show the grouped bar chart
plt.margins(0.05, 0.15)
plt.tight_layout()
plt.show()
