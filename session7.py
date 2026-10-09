# task1
import pandas as pd

# Load Zomato ratings CSV
df = pd.read_csv("zomato_ratings.csv")

# Calculate Q1 and Q3
Q1 = df["user_rating"].quantile(0.25)
Q3 = df["user_rating"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Detect outliers
outliers = df[
    (df["user_rating"] < lower_limit) |
    (df["user_rating"] > upper_limit)
]

# Print indices of outliers
print("Outlier indices:")
print(outliers.index.tolist())
print("\nOutlier values:")
print(outliers["user_rating"])


# task2
import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

# Load Swiggy orders dataset
df = pd.read_csv("swiggy_orders.csv")

# Create boxplot
plt.boxplot(df["order_amount"].dropna())

# Label axes
plt.xlabel("Swiggy Orders")
plt.ylabel("Order Amount")
plt.title("Boxplot of Swiggy Order Amounts")

# Display plot
plt.show()


# task3
Q1 = df["order_amount"].quantile(0.25)
Q3 = df["order_amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[
    (df["order_amount"] < lower) |
    (df["order_amount"] > upper)
]
print("Outliers:")
print(outliers["order_amount"])


# task4
import pandas as pd

# Sample Flipkart DataFrame
df = pd.DataFrame({
    "product": ["Laptop", "Mobile", "Headphones", "Monitor"],
    "price": ["₹1,299", "₹25,999", "₹999", "₹15,499"]
})

print("Before conversion:")
print(df)
print(df["price"].dtype)

# Remove ₹ and commas
df["price"] = df["price"].str.replace("₹", "", regex=False)
df["price"] = df["price"].str.replace(",", "", regex=False)

# Convert to numeric
df["price"] = df["price"].astype(float)

print("\nAfter conversion:")
print(df)
print(df["price"].dtype)


# task5
# doubt