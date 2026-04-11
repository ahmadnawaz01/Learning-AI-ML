# 1. Creating a Tuple
# Tuples use parentheses ()
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)

print(f"Original Tuple: {my_tuple}")
print("-" * 35)

# 2. Method: count()
# Returns the number of times a specified value occurs
count_of_seven = my_tuple.count(7)
print(f"Count of number 7: {count_of_seven}") # Output: 3

# 3. Method: index()
# Searches the tuple for a specified value and returns its FIRST position
# Note: It raises a ValueError if the value is not found
index_of_eight = my_tuple.index(8)
print(f"First index of number 8: {index_of_eight}") # Output: 3

# 4. Built-in Functions (Commonly used with Tuples)
print(f"Length of tuple: {len(my_tuple)}")
print(f"Maximum value:   {max(my_tuple)}")
print(f"Minimum value:   {min(my_tuple)}")
print(f"Sum of values:   {sum(my_tuple)}")

# 5. Accessing by Index (Slicing)
print(f"First three:     {my_tuple[:3]}")
print(f"Last item:       {my_tuple[-1]}")