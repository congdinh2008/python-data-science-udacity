import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a DataFrame
df = pd.read_csv("q_02.csv")

# Get unique categories and rental durations and sort categories alphabetically
categories = sorted(df['category_name'].unique())
rental_durations = df['rental_duration'].unique()

# Create a dictionary to store movie counts for each category and rental duration
data_dict = {rental_duration: [] for rental_duration in rental_durations}

# Group the data by rental duration and category
for rental_duration in rental_durations:
    for category in categories:
        subset = df[(df['rental_duration'] == rental_duration)
                    & (df['category_name'] == category)]
        data_dict[rental_duration].append(subset['film_title'].count())

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Define the width of each bar and the positions for each group
width = 0.15
x = np.arange(len(categories))

# Create bars for each rental duration
for i, rental_duration in enumerate(rental_durations):
    bars = ax.bar(x + i * width, data_dict[rental_duration],
                  width=width, label=f'Rental {rental_duration}')

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
ax.set_title("Movie Distribution by Category for Each Rental Duration",
             fontsize=12, fontweight='bold')
ax.set_xticks(x + width * (len(rental_durations) - 1) / 2)
ax.set_xticklabels(categories)
ax.legend(title="Rental Duration")

# Show the grouped bar chart
plt.tight_layout()
plt.show()
