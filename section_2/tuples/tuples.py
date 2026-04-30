my_tuple = 'Ford', 'Escort', 1300, 'Red'
my_tuple = ('Ford', 'Escort', 1300, 'Red')

print(my_tuple)

my_single_element_tuple = 'Ford',
print(my_single_element_tuple)

#creation of empty tuple
my_empty_tuple = ()
my_empty_tuple = tuple()

#error immutable
#my_tuple[1] = 'Fiesta'

print(my_tuple[0])
print(my_tuple[3])
print(my_tuple[-1])  # ACCESSING FROM THE END
print(my_tuple[-2])

print( my_tuple.count('Ford') ) 

fruits = ("apple", "apple", "banana", "banana", "banana", "tangerine")
print(fruits.count("banana") ) 

print(my_tuple.index("Escort") ) 

print(len(my_tuple)) 


