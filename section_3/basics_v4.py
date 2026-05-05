# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)

# 2. Print the difference between the largest and smallest value:

print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

previous_number = 0
for number in numbers:
    if number == 2 and previous_number == 2:
        print("True")
    else:
        previous_number = number

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
total = 0
breaker = False

for number in numbers:
    if number == 6:
        breaker = True
    if number == 7:
        breaker = False
    if breaker == False:
        total += number

print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

no_unlucky_numbers_total = 0
is_previous_index_13 = False

for number in numbers:
    if number != 13 and not is_previous_index_13:
        no_unlucky_numbers_total += number
        is_previous_index_13 = False
    if number == 13:
        is_previous_index_13 = True
    if number != 13 and is_previous_index_13:
        is_previous_index_13 = False


print(no_unlucky_numbers_total)





