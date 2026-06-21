import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    'data/superstore.csv',
    encoding='latin1'
)

# Sales by Category
sales_by_category = (
    df.groupby('Category')['Sales']
      .sum()
      .sort_values(ascending=False)
)

# Plot
plt.figure(figsize=(8,5))

sales_by_category.plot(kind='bar')

plt.title('Sales by Category')

plt.xlabel('Category')

plt.ylabel('Total Sales')

plt.xticks(rotation=0)

plt.tight_layout()

# Save image
plt.savefig('outputs/sales_by_category.png')

# Show chart
plt.show()



# Profit by Category

profit_by_category = (
    df.groupby('Category')['Profit']
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

profit_by_category.plot(kind='bar')

plt.title('Profit by Category')

plt.xlabel('Category')

plt.ylabel('Total Profit')

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig('outputs/profit_by_category.png')

plt.show()



# Correlation Heatmap

corr = df[
    ['Sales', 'Profit', 'Discount', 'Quantity']
].corr()

plt.figure(figsize=(6,4))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')

plt.tight_layout()

plt.savefig('outputs/correlation.png')

plt.show()



# =====================================================
# Monthly Sales Trend
# =====================================================

# Convert Order Date to datetime

df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year-Month

df['Month'] = df['Order Date'].dt.to_period('M')

# Total Sales per Month

monthly_sales = (
    df.groupby('Month')['Sales']
      .sum()
)

# Convert Period to string for plotting

monthly_sales.index = monthly_sales.index.astype(str)

# Plot

plt.figure(figsize=(12,5))

monthly_sales.plot(kind='line')

plt.title('Monthly Sales Trend')

plt.xlabel('Month')

plt.ylabel('Total Sales')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('outputs/sales_trend.png')

plt.show()