# Angel Chavez
# Aug 4th, 2025
# Python 3.13.5
# program that showcases "NumPy" by analyzing and manipulating game score data.
# numpy provides an array object, these array objects are more efficient than lists. 

import numpy as np      # this is standard convention

scores = np.array([85, 92, 76, 100, 67, 89, 94, 55, 73, 88])

average = np.mean(scores)
highest = np.max(scores)
lowest = np.min(scores)
bonus_scores = scores + 5

# boolean mask where True indacates elements in scores >90, and False if not
# mask is then used as an index for scores to print out the elements where mask is True
mask = scores > 90
above_90_scores = scores[mask]

# counts how many scores are either above or below 70, then sums them up
passing_count = (scores >= 70).sum()
failing_count = (scores < 70).sum()

# sorts scores in ascending order
sorted_scores = np.sort(scores)

# normalizes scores to a 0-1 scale using min-max normalization
normalized_scores = (scores - lowest) / (highest - lowest)

print(f'Original scores: {scores}')
print(f'Average score: {average}')
print(f'Highest score: {highest}')
print(f'Lowest score: {lowest}')
print(f'Scores above 90: {above_90_scores}')
print(f'Passing scores(>=70): {passing_count} passed')
print(f'Failing scores(<70): {failing_count} failed')
print(f'Sorted Scores: {sorted_scores}')
print(f'Min-Max normalized scores 0-1: {normalized_scores}')
print(f'Scores after +5 bonus: {bonus_scores}')