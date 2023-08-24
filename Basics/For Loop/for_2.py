
#* Problem 2: Sum of ALL numbers in a given list.
# Given a list of numbers, use a "for" loop to calculate and print the sum of all the numbers.
# Examples: for input "[1, 2, 3]" output will be "6"

#* Solution:

numbers = [1, 2, 3]
sum = 0
for number in numbers:
    sum += number
print(sum)  

#* Output:
# 6

#* Explanation:
# The `sum` variable is initialized to 0. Then, the `for` loop iterates through each number in the list. Each time through the loop, the `sum` variable is updated to be the previous value of `sum` plus the current number. Finally, the `sum` variable is printed.

