# task 1
# pyrefly: ignore [missing-import]
import numpy as np

ratings = np.array([
    [4, 5, 3, 4, 5],  # User 1
    [5, 4, 4, 3, 5],  # User 2
    [3, 5, 4, 5, 4],  # User 3
    [4, 3, 5, 4, 3]   # User 4
])

print("All ratings:")
print(ratings)

# Extract ratings given by the second and third users
selected_ratings = ratings[1:3]
print("\nRatings of User 2 and User 3:")
print(selected_ratings)

# task2
# pyrefly: ignore [missing-import]
import numpy as np
steps = np.array([7500, 8200, 9000, 6500, 10000, 7800, 8500, 7200, 9500, 8100])

# Boolean indexing
high_steps = steps[steps > 8000]
print("\nDaily steps:")
print(steps)
print("\nSteps greater than 8000:")
print(high_steps)

# task3
# pyrefly: ignore [missing-import]
import numpy as np
ipl_scores = np.array([185, 210, 167, 198, 225, 174, 201, 190])
print("\nIPL scores:")
print(ipl_scores)

# Select scores from matches 2, 5, and 7
selected_scores = ipl_scores[[1, 4, 6]]
print("\nScores from matches 2, 5, and 7:")
print(selected_scores)

# task4
# pyrefly: ignore [missing-import]
import numpy as np
prices = np.array([1000, 2500, 5000, 750, 1200])
# Apply 10% discount using broadcasting
discounted_prices = prices * 0.90
print("\nOriginal prices:")
print(prices)
print("\nPrices after 10% discount:")
print(discounted_prices)

# task5
# pyrefly: ignore [missing-import]
import numpy as np
ratings = np.array([-2, 5, 3, -1, 0, 4, -5, 2, 1])
print("\nOriginal ratings:")
print(ratings)

# Create a Boolean mask for negative ratings
ratings[ratings < 0] = 0
print("\nRatings after replacing negative values with zero:")
print(ratings)
