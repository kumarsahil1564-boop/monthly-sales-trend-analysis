import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("sales_data.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Group sales by month
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

# Format month
monthly_sales["Month"] = monthly_sales["Order_Date"].dt.strftime("%B %Y")

# Display monthly summary
print("Monthly Sales Summary")
print(monthly_sales[["Month", "Sales"]])

# Create line chart
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig("monthly_sales_trend.png")

plt.show()
