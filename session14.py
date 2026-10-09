# task1
import pandas as pd

# Load the IPL dataset
df = pd.read_csv("ipl_matches.csv")

# Display first five rows
print(df.head())

# Summary statistics for total_runs
print("Mean:", df["total_runs"].mean())
print("Median:", df["total_runs"].median())
print("Minimum:", df["total_runs"].min())
print("Maximum:", df["total_runs"].max())
print("Standard Deviation:", df["total_runs"].std())


# task2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Flipkart review data
df = pd.DataFrame({
    "rating": [5, 4, 3, 5, 1, 4, 2, 5, 3, 4, 1, 5, 2, 4, 3],
    "category": [
        "Mobile", "Fashion", "Electronics", "Mobile", "Fashion",
        "Mobile", "Home", "Electronics", "Home", "Fashion",
        "Mobile", "Home", "Electronics", "Mobile", "Fashion"
    ]
})

# Count reviews for each rating
sns.countplot(data=df, x="rating", order=[1, 2, 3, 4, 5])
plt.title("Count of Flipkart Reviews by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Reviews")
plt.show()


# task3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Zomato restaurant data
df = pd.DataFrame({
    "average_cost_for_two": [300, 500, 800, 1200, 1500, 400, 900, 2000],
    "user_rating": [3.2, 3.8, 4.1, 4.5, 4.6, 3.5, 4.0, 4.7]
})

# Create scatterplot
sns.scatterplot(
    data=df,
    x="average_cost_for_two",
    y="user_rating"
)
plt.title("Restaurant Cost vs User Rating")
plt.xlabel("Average Cost for Two (₹)")
plt.ylabel("User Rating")
plt.show()


# task4
# doubt


# task5
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Spotify songs data
df = pd.DataFrame({
    "danceability": [0.80, 0.65, 0.45, 0.90, 0.70, 0.55, 0.85, 0.60],
    "energy":       [0.90, 0.70, 0.40, 0.95, 0.75, 0.50, 0.85, 0.65],
    "valence":      [0.85, 0.60, 0.30, 0.90, 0.70, 0.40, 0.80, 0.55],
    "popularity":   [85, 70, 45, 95, 75, 50, 88, 65]
})

# Create pairplot
sns.pairplot(
    df[["danceability", "energy", "valence", "popularity"]]
)
plt.show()