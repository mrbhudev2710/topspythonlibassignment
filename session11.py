# task1
import matplotlib.pyplot as plt

# Sample data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [20, 35, 30, 45, 50]

products = ["Pizza", "Burger", "Biryani", "Pasta"]
orders = [40, 30, 20, 25]

ratings = [3.5, 4.0, 4.2, 4.5, 4.8]
prices = [200, 300, 350, 450, 500]

platforms = ["Swiggy", "Zomato", "Dominos"]
orders_platform = [40, 35, 25]

# Create 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line chart
axes[0, 0].plot(days, sales, marker="o")
axes[0, 0].set_title("Daily Sales")
axes[0, 0].set_xlabel("Days")
axes[0, 0].set_ylabel("Sales")

# 2. Bar chart
axes[0, 1].bar(products, orders)
axes[0, 1].set_title("Orders by Product")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Orders")

# 3. Scatter plot
axes[1, 0].scatter(ratings, prices)
axes[1, 0].set_title("Rating vs Price")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Price")

# 4. Pie chart
axes[1, 1].pie(
    orders_platform,
    labels=platforms,
    autopct="%1.1f%%"
)
axes[1, 1].set_title("Orders by Platform")

plt.tight_layout()
plt.show()


# task2
import matplotlib.pyplot as plt

platforms = ["Zomato", "Swiggy", "Domino's"]
delivery_time = [32, 28, 35]

colors = ["red", "orange", "blue"]
linestyles = ["-", "--", ":"]
linewidths = [2, 3, 4]

fig, ax = plt.subplots()

for i in range(len(platforms)):
    ax.plot(
        platforms[i],
        delivery_time[i],
        marker="o",
        color=colors[i],
        linestyle=linestyles[i],
        linewidth=linewidths[i],
        markersize=10,
        label=platforms[i]
    )

ax.set_xlabel("Food Delivery Platform")
ax.set_ylabel("Average Delivery Time (Minutes)")
ax.set_title("Average Delivery Time Comparison")

ax.legend()

plt.show()


# task3
import matplotlib.pyplot as plt

influencers = ["A", "B", "C", "D", "E"]

followers = [100000, 250000, 500000, 750000, 1000000]
daily_posts = [2, 3, 1, 4, 5]

fig, ax1 = plt.subplots()

# Left Y-axis - Followers
ax1.plot(
    influencers,
    followers,
    color="blue",
    marker="o",
    linewidth=2,
    label="Followers"
)

ax1.set_xlabel("Influencers")
ax1.set_ylabel("Instagram Followers")

# Right Y-axis
ax2 = ax1.twinx()

ax2.plot(
    influencers,
    daily_posts,
    color="red",
    marker="s",
    linewidth=2,
    label="Daily Posts"
)

ax2.set_ylabel("Average Daily Posts")

plt.title("Instagram Followers vs Average Daily Posts")

plt.show()


# task4
import matplotlib.pyplot as plt

movies = [
    "Jawan",
    "Pathaan",
    "Animal",
    "Stree 2",
    "Dangal"
]

tickets = [150, 130, 120, 100, 180]
ratings = [7.0, 5.8, 6.1, 7.0, 8.3]

plt.scatter(tickets, ratings, s=100)

# Add movie names above points
for i in range(len(movies)):
    plt.annotate(
        movies[i],
        (tickets[i], ratings[i]),
        xytext=(5, 5),
        textcoords="offset points"
    )

# plt.xlabel("Tickets Sold (Lakhs)")
plt.ylabel("IMDb Rating")
plt.title("Bollywood Movies: Tickets Sold vs IMDb Rating")

plt.show()