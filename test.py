# write a function that takes a list of numbers and returns the sum of the squares of all the numbers.

def sum_of_squares(nums):
    return sum([num ** 2 for num in nums])


print(sum_of_squares([2, 3, 4]))  # should be 29
print(sum_of_squares([0, 1, 2]))  # should be 5
print(sum_of_squares([]))  # should be 0
print(sum_of_squares([2, -3, 4]))  # should be 29
print(sum_of_squares([2.5, 3.5, 4.5]))  # should be 50.5
