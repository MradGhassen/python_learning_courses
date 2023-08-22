# 1 Countdown - Create a function that accepts a number as an input. Return a new list 
#   that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def Countdown(number):
    new_list = []
    for i in range(number,-1,-1):
        new_list.append(i)
    return new_list
print(Countdown(5))

# 2 Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.

def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

# 3 First Plus Length - Create a function that accepts a list and returns the sum of the first 
# value in the list plus the list's length.

def First_Plus_Length (list):
    sum = list[0] + len(list)
    return sum
print(First_Plus_Length([1,2,3,4,5]))

# 4 Values Greater than Second - Write a function that accepts a list and creates a new list 
# containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements,
# have the function return False

def Values_Greater_than_Second (list):
    if len(list) < 2:
        return False
    new_list = []
    for i in list:
        if i > list[1]:
            new_list.append(i)
    return new_list
print(Values_Greater_than_Second([3]))
print(Values_Greater_than_Second([5,2,3,2,1,4]))

# 5 This Length, That Value - Write a function that accepts two integers as parameters: size and value.
#  The function should create and return a list whose length is equal to the given size,
#  and whose values are all the given value.

def This_Length_That_Value (size,value):
    list = []
    for i in range (size):
     list.append(value)
    return list 
print(This_Length_That_Value(4,7))
print(This_Length_That_Value(6,2))