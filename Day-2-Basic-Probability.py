# Set data
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
total_possibilities = 0

# Verify possibilities
for i in range(len(dice1)):
    for j in range(len(dice2)):
        if (dice1[j] + dice1[i]) <= 9:
            total_possibilities = total_possibilities + 1
            print("{0} + {1} = {2}".format(dice1[i], dice2[j], (dice1[j] + dice1[i])))

# Get probability
probability = total_possibilities / total
print("Probability: {0}/{1} = {2}".format(total_possibilities,total,probability))

================================
We have two fair dice, let's lay out all the possible outcomes in a grid to make easier calcuation The total number of possible outcomes = 6C1 * 6C1 = 36

(1,1)(1,2)(1,3)(1,4)(1,5)(1,6)
(2,1)(2,2)(2,3)(2,4)(2,5)(2,6)
(3,1)(3,2)(3,3)(3,4)(3,5)(3,6)
(4,1)(4,2)(4,3)(4,4)(4,5)(4,6)
(5,1)(5,2)(5,3)(5,4)(5,5)(5,6)
(6,1)(6,2)(6,3)(6,4)(6,5)(6,6)

For challenge 1, to find outcomes which sum to a max of 9, we can see that only 6 combinations do not satisfy this condition.
Imagine a diagonal from (6,3) to (3,6) and everything to the right of that line sums more than 9.
Total no of favourable outcomes = 36 - 6 = 30
P(event) = Fav. outcomes/Total outcomes = 30/36 = 5/6
