import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv("q_01.csv")

# Prepare the data for plotting
df['rental_date'] = df['rental_month'].astype(
    str) + '/' + df['rental_year'].astype(str)
pivot_df = df.pivot(index='rental_date', columns='store_id', values='count_rentals').fillna(
    0).sort_values("rental_date", ascending=False)

# Plot the data using a bar chart
ax = pivot_df.plot(kind='bar', figsize=(12, 6))

# Customize the chart labels and title
plt.xlabel("Time Series", fontsize=10, fontweight='bold')
plt.ylabel("Count of Rentals", fontsize=10, fontweight='bold')
plt.title("Count of Rentals by Month, Year, and Store",
          fontsize=12, fontweight='bold')

# Show the legend
plt.legend(title="Store ID")

# Add annotations (count_rentals) at the top of each bar
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() +
                p.get_width() / 2., p.get_height()), ha='center', va='bottom')

# Display the chart
plt.show()
