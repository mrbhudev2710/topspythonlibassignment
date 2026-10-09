# task1
import pandas as pd
import numpy as np

timestamps = [
    '2024-06-01 14:30',
    '2024-06-02 09:15',
    '2024-06-03 20:45'
]

df = pd.DataFrame({"delivery_time": timestamps})
df["delivery_time"] = pd.to_datetime(df["delivery_time"])

print(df)
print(df["delivery_time"].dtype)


# task2
import pandas as pd
import numpy as np

df = pd.read_csv("orders.csv")

# Convert order_date into datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract year, month and weekday
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["weekday"] = df["order_date"].dt.day_name()

print(df)


# task3
import pandas as pd
import numpy as np

df = pd.read_csv("orders.csv")

# Convert to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Set order_date as index
df = df.set_index("order_date")

# Count orders placed each week
weekly_orders = df.resample("W").size()

print(weekly_orders)


# task4
import pandas as pd
import numpy as np

data = {
    "posted_at": [
        "2024-06-01 10:00:00",
        "2024-06-02 12:30:00",
        "2024-06-03 15:45:00",
        "2024-06-04 08:20:00",
        "2024-06-05 18:10:00"
    ]
}

df = pd.DataFrame(data)

# Convert to UTC datetime
df["posted_at"] = pd.to_datetime(df["posted_at"], utc=True)

# Convert UTC to Asia/Kolkata
df["posted_at_kolkata"] = df["posted_at"].dt.tz_convert("Asia/Kolkata")

# Display first 5
print(df["posted_at_kolkata"].head(5))


# task5
# doubt