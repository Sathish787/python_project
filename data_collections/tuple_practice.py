sample_tuple = ('TV', 'Computer', 'Laptop', 'fridge', [1, 2, 3])
# Definition:
# A tuple is a collection of objects which ordered and immutable (unchangeable). It is similar to list.
# The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# Advantages of Tuple over List in Python:
# Since tuples are quite similar to lists, both of them are used in similar situations.
# However, there are certain advantages of implementing a tuple over a list:
# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

# Printing tuple
print(f'The tuple elements are : {sample_tuple}')

# Accessing tuple element by index
print(f'Print second element of tuple: {sample_tuple[1]}')

# Accessing tuple element by negative index
print(f'Print last element of tuple: {sample_tuple[-1]}')

# Iterating all elements in tuple by using for in loop
for item in sample_tuple:
    print(f'Printing all items/elements in the tuple: {item}')


# Getting length of tuple
print(f'Length of the tuple: {str(len(sample_tuple))}')

# Iterating and accessing tuple elements by index
for i in range(len(sample_tuple)):
    print(f'Index of tuple: {str(i)}')

# Iterating and accessing tuple elemnts and its index
for i, value in enumerate(sample_tuple):
    print(f'The tuple index: {i} and value: {value}')

# Using iterator to iterate tuple
sample_iter = iter(sample_tuple)
print(f'Iterate tuple using iter and next: {next(sample_iter)}')
print(f'Iterate tuple using iter and next: {next(sample_iter)}')
print(f'Iterate tuple using iter and next: {next(sample_iter)}')

# Slicing - Access a range of items in a tuple by using the slicing operator colon
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])

# elements beginning to 2nd
print(my_tuple[:-7])


# elements 8th to end
print(my_tuple[7:])

# elements beginning to end
print(my_tuple[:])


# Check if an Item Exists in the Python Tuple
languages = ('Python', 'Swift', 'C++')

print('C' in languages)  # output: False
print('Python' in languages)  # output: True

# Python Tuple Methods
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# 1. Count
print(my_tuple.count('p'))  # output: 2

# 2. Index
print(my_tuple.index('l'))  # output: 3

