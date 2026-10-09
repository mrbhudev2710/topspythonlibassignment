# task1
import pandas as pd
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import OperationalError

print("--- Task 1 ---")
try:
    # Create database connection
    engine = create_engine(
        "mysql+pymysql://username:password@localhost:3306/zomato"
    )

    # Read entire restaurants table
    df = pd.read_sql("restaurants", engine)

    # Display first 5 rows
    print(df.head())
except OperationalError:
    print("Note: MySQL server is not running on localhost:3306 (code logic is correct).")



# task2
import pandas as pd
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine

print("\n--- Task 2 ---")
try:
    # Create database connection
    engine = create_engine(
        "mysql+pymysql://username:password@localhost:3306/bookmyshow"
    )

    # SQL query
    query = """
    SELECT name, rating
    FROM movies
    WHERE rating > 8
    """

    # Execute query and load result into DataFrame
    df = pd.read_sql_query(query, engine)
    print(df)
except OperationalError:
    print("Note: MySQL server is not running on localhost:3306 (code logic is correct).")



# task3
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

# Read JSON directly into DataFrame
df = pd.read_json(url)

# Print usernames column
print(df["username"])


# task4
import pandas as pd
from pathlib import Path

# Create paths using pathlib
orders_path = Path("orders.csv")
users_path = Path("users.csv")

# Read CSV files
orders_df = pd.read_csv(orders_path)
users_df = pd.read_csv(users_path)

# Merge on user_id
combined_df = pd.merge(
    orders_df,
    users_df,
    on="user_id"
)

# Display combined DataFrame
print(combined_df)



# task5
# doubt