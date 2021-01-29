# Mean Median & Mode
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))



# Weighted Mean
size = int(input())
numbers = list(map(int, input().split()))
weighted = list(map(int, input().split()))

sum_items = 0
for i in range(size):
    sum_items = sum_items + (numbers[i] * weighted[i])

print(round(sum_items/sum(weighted), 1))