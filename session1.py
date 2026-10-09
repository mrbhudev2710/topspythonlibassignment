# task1
# already done

# task2
# pyrefly: ignore [missing-import]
import numpy as np
followers = np.array([1200, 15000, 67000, 340000, 1250000])
print("Followers:", followers)
print("Shape:", followers.shape)
print("Number of dimensions:", followers.ndim)
print("Data type:", followers.dtype)

#task3
# pyrefly: ignore [missing-import]
import numpy as np
order_ids = np.arange(101, 111)
print("Order IDs:", order_ids)
print("Size:", order_ids.size)


#task4
# pyrefly: ignore [missing-import]
import numpy as np
like_matrix = np.eye(3)
# The diagonal values of 1 represent a like/identity relationship
# for each corresponding playlist item or user.
print("Spotify Like Identity Matrix:")
print(like_matrix)

#task5
# pyrefly: ignore [missing-import]
import numpy as np
cricket_scores = [45, 67, 120, 89, 54]
scores_array = np.array(cricket_scores)
print("Cricket Scores:", scores_array)
print("Bytes used by each score:", scores_array.itemsize)