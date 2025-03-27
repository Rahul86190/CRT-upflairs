'''
 How do lists and tuples differ in terms of mutability and 
performance? When would you choose one over the other?'''

# Lists are mutable, tuples are immutable.
# Lists are faster than tuples.
# Use lists when you have a collection of items that may change,
# and tuples when you have a collection of items that will not change.

# Example:

# List
l = [1, 2, 3]
l[0] = 4
print(l) # [4, 2, 3]

print("\n")

# Tuple
t = (1, 2, 3)
# t[0] = 4 # TypeError: 'tuple' object does not support item assignment
print(t[0])