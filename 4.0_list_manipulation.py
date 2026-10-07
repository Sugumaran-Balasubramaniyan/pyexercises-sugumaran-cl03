"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What my list is about, and what I computed from it:


# Your code below
number_1 = 2
number_2 = 3
number_3 = 4
number_4 = 5

print(number_1)
print(number_2)
print(number_3)
print(number_4)

list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]
print("Listing all the numbers in the list")
print(list_of_numbers)
print("Listing the third item in the list")
print(list_of_numbers[2])

# sorting the list 
print("The list of numbers after sorted ")
list_of_numbers.sort()
print(list_of_numbers)

# removing the last item from the list
list_of_numbers.pop()

# list of numbers after removing the last 
print("The list of numbers of numbers after removing the last item from the list")
print(list_of_numbers)