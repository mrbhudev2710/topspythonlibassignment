# task1
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate 50 random delivery times
np.random.seed(10)
delivery_times = np.random.randint(20, 61, 50)

# Create histogram
sns.histplot(delivery_times, bins=8, kde=True)

plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Number of Orders")
plt.title("Distribution of Zomato Delivery Times")

plt.show()


# task2
import seaborn as sns
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset("tips")

# Create boxplot
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.title("Distribution of Total Bills by Day")

plt.show()


# task3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set darkgrid theme
sns.set_theme(style="darkgrid")

teams = [
    "CSK", "MI", "RCB", "KKR",
    "DC", "PBKS", "RR", "SRH"
]

# Generate IPL scores
np.random.seed(20)

data = []

for team in teams:
    scores = np.random.randint(120, 220, 20)

    for score in scores:
        data.append([team, score])

df = pd.DataFrame(data, columns=["Team", "Runs"])

# Create violin plot
sns.violinplot(
    data=df,
    x="Team",
    y="Runs"
)

plt.xlabel("IPL Teams")
plt.ylabel("Runs")
plt.title("IPL Run Distribution by Team")

plt.show()


# task4
# doubt


# task5
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Whitegrid theme
sns.set_theme(style="whitegrid")

# Daily step counts
steps = [
    4500, 5200, 6000, 5800,
    7000, 7500, 8000
]

# KDE plot
sns.kdeplot(
    steps,
    fill=True,
    color="green"
)

plt.xlabel("Daily Steps")
plt.ylabel("Density")
plt.title("Distribution of Daily Step Counts")

plt.show()