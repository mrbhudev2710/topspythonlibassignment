# task1
# already done



# task2
import pandas as pd

# Read JSON file
df = pd.read_json("trending_songs.json")

# Display the DataFrame
print(df)

# Display column names and data types
df.info()



# task3
import pandas as pd

# Read TSV file
df = pd.read_csv("zomato_restaurants.tsv", sep="\t")

# Display the data
print(df)

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))


# task4
import pandas as pd

# Read the Excel file
df = pd.read_excel("flipkart_products.xlsx")

# Process 2000 rows at a time
chunk_size = 2000
for start in range(0, len(df), chunk_size):
    chunk = df.iloc[start:start + chunk_size]
    print("Rows in this chunk:", len(chunk))


# task5
import pandas as pd

# Read semicolon-separated CSV
df = pd.read_csv("paytm_transactions.csv", sep=";")
print("Paytm Transactions:")
print(df)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Print only columns that contain null values
print("\nColumns containing null values:")
null_columns = df.columns[df.isnull().any()]
for column in null_columns:
    print(column)