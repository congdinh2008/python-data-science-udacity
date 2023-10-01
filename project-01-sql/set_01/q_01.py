import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv("q_01.csv")

category_data = df.groupby('category_name')['rental_count'].sum()

# Create a line chart
plt.bar(category_data.index, category_data.values)

# Add labels and title
plt.xlabel("Category Name", fontsize=10, fontweight='bold')
plt.ylabel("Number of Rentals", fontsize=10, fontweight='bold')
plt.title("Total Rental Count by Category", fontsize=12, fontweight='bold')

# Add labels on top of the bars
for i, v in enumerate(category_data.values):
    plt.text(i, v + 5, str(v), ha='center', va='bottom')

# Show the chart
plt.show()
