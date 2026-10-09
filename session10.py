# task 1
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [4500, 6200, 5800, 7500, 6800, 9000, 8200]

plt.plot(days, steps, marker="o")
plt.xlabel("Days")
plt.ylabel("Number of Steps")
plt.title("Daily Steps for Last 7 Days")
plt.grid(True)

# Save chart
plt.savefig("steps_lineplot.png")
plt.show()


# task2
import matplotlib.pyplot as plt

restaurants = [
    "Dominos", "McDonalds", "KFC", "Subway", "Pizza Hut",
    "Burger King", "Haldiram", "Barbeque Nation", "Cafe Coffee Day", "Biryani House"
]

ratings = [4.2, 4.0, 4.1, 4.3, 4.0, 4.1, 4.4, 4.5, 3.9, 4.2]
meal_price = [500, 350, 450, 400, 550, 400, 600, 1200, 300, 450]

plt.scatter(ratings, meal_price)
plt.xlabel("Zomato Rating")
plt.ylabel("Average Meal Price (₹)")
plt.title("Zomato Ratings vs Average Meal Price")
plt.show()


# task3
import matplotlib.pyplot as plt

apps = ["Swiggy", "Zomato", "Domino's"]
orders = [18, 25, 12]
colors = ["blue", "red", "orange"]

plt.bar(apps, orders, color=colors, label="Orders")
plt.xlabel("Food Delivery Platform")
plt.ylabel("Number of Orders")
plt.title("Food Orders in Last Month")
plt.legend()
plt.show()


# task4
import matplotlib.pyplot as plt

durations = [
    20, 35, 45, 50, 30,
    60, 75, 40, 55, 25,
    90, 65, 45, 35, 50,
    80, 70, 40, 30, 60
]

plt.hist(durations, bins=5, color="purple", edgecolor="black")
plt.xlabel("Listening Duration (Minutes)")
plt.ylabel("Number of Sessions")
plt.title("Spotify Listening Session Duration")
plt.show()


# task5
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

screen_time = [2.5, 3, 2, 4, 3.5, 5, 4.5]
posts_liked = [10, 15, 8, 20, 18, 30, 25]

# Create two subplots
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

# First subplot - Line Plot
axes[0].plot(days, screen_time, marker="o")

axes[0].set_title("Daily Instagram Screen Time")
axes[0].set_xlabel("Days")
axes[0].set_ylabel("Screen Time (Hours)")

# Second subplot - Bar Chart
axes[1].bar(days, posts_liked)

axes[1].set_title("Instagram Posts Liked Each Day")
axes[1].set_xlabel("Days")
axes[1].set_ylabel("Posts Liked")

# Adjust spacing
plt.tight_layout()

# Save figure
plt.savefig("social_media_usage.png")

plt.show()