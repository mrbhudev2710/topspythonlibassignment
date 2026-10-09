# task1
import pandas as pd

data = {
    "Restaurant": ["Dominos", "McDonalds", "Dominos", "KFC", "Dominos"],
    "Order_Date": ["2026-10-01", "2026-10-02", "2026-10-01", "2026-10-03", "2026-10-04"]
}

df = pd.DataFrame(data)

# Find duplicate orders based on Restaurant and Order_Date
duplicates = df[df.duplicated(subset=["Restaurant", "Order_Date"], keep=False)]

print("Duplicate Orders:")
print(duplicates)


# task2
import pandas as pd

reviews = [
    "Good product",
    "Excellent quality",
    "Good product",
    "Nice product",
    "Good product",
    "Excellent quality",
    "Nice product",
    "Good product"
]

df = pd.DataFrame({"Review": reviews})

# Count repeated reviews
review_counts = df["Review"].value_counts()

# Display top 3
print("Top 3 Most Common Reviews:")
print(review_counts.head(3))


# task3
import pandas as pd

data = {
    "Playlist_Name": [
        "Workout Hits",
        "Chill Vibes",
        "Workout Hits",
        "Party Songs",
        "Chill Vibes"
    ],
    "Creator": [
        "Jiya",
        "Rahul",
        "Jiya",
        "Neha",
        "Rahul"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Remove exact duplicate rows
cleaned_df = df.drop_duplicates()

print("\nCleaned DataFrame:")
print(cleaned_df)


# task4
import pandas as pd

data = {
    "Username": [
        "insta_queen",
        "insta-queen",
        "instaqueen",
        "insta_queen",
        "insta-queen"
    ]
}

df = pd.DataFrame(data)

# Standardize all variants
df["Username"] = df["Username"].replace({
    "insta_queen": "instaqueen",
    "insta-queen": "instaqueen"
})

print(df)


# task5
import pandas as pd

data = {
    "Payment_Status": [
        "Yes",
        "yes",
        " Y ",
        "No",
        "no",
        " N ",
        " YES "
    ]
}

df = pd.DataFrame(data)

# Remove extra spaces and convert to lowercase
df["Payment_Status"] = (
    df["Payment_Status"]
    .str.strip()
    .str.lower()
)

# Convert Yes/Y to 1 and No/N to 0
df["Payment_Status"] = df["Payment_Status"].replace({
    "yes": 1,
    "y": 1,
    "no": 0,
    "n": 0
})

print(df)