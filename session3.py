# task1
import numpy as np

friend1 = np.array([7500, 8200, 9000, 6500, 10000, 7800, 8500])
friend2 = np.array([7000, 8500, 8800, 7200, 9500, 8000, 9000])

print("Friend 1 steps:")
print(friend1)

print("\nFriend 2 steps:")
print(friend2)

# Element-wise addition
addition = friend1 + friend2
print("\nAddition:")
print(addition)

# Element-wise subtraction
subtraction = friend1 - friend2
print("\nSubtraction:")
print(subtraction)

# Element-wise multiplication
multiplication = friend1 * friend2
print("\nMultiplication:")
print(multiplication)

# Element-wise division
division = friend1 / friend2
print("\nDivision:")
print(division)


# task2
import numpy as np

user_preferences = np.array([
    [5, 2, 3],
    [4, 5, 1],
    [2, 4, 5]
])

song_popularity = np.array([
    [5, 4, 2],
    [3, 5, 4],
    [2, 3, 5]
])

# Using dot()
recommendation_dot = np.dot(user_preferences, song_popularity)

# Using matmul()
recommendation_matmul = np.matmul(user_preferences, song_popularity)

print("User Preferences:")
print(user_preferences)

print("\nSong Popularity:")
print(song_popularity)

print("\nRecommendation Matrix using dot():")
print(recommendation_dot)

print("\nRecommendation Matrix using matmul():")
print(recommendation_matmul)


# task3
import numpy as np

pixels = np.array([
    [120, 150, 180, 200],
    [100, 130, 160, 190],
    [90, 140, 170, 210],
    [110, 125, 155, 195]
])

print("Original pixel matrix:")
print(pixels)

# Transpose the matrix
transposed = pixels.T

print("\nTransposed matrix:")
print(transposed)

# Statistical calculations
mean_value = np.mean(pixels)
median_value = np.median(pixels)
standard_deviation = np.std(pixels)
variance = np.var(pixels)

print("\nMean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", standard_deviation)
print("Variance:", variance)


# task4
# doubt

# task5
# doubt