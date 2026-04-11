# Initializing a list
fruits = ["apple", "banana", "cherry"]
print(f"Original List: {fruits}")
print("-" * 30)

# 1. Adding Elements
fruits.append("orange")          # Adds to the END
fruits.insert(1, "blueberry")    # Adds at INDEX 1
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)       # Adds another list to the end
print(f"After Adding: {fruits}")

# 2. Removing Elements
fruits.remove("banana")          # Removes specific ITEM (first occurrence)
popped_item = fruits.pop(2)      # Removes & returns item at INDEX 2
del fruits[0]                    # Removes item at INDEX 0 using 'del' keyword
# fruits.clear()                 # Use this to empty the entire list
print(f"After Removing: {fruits} (Popped: {popped_item})")

# 3. Searching & Counting
index_of_mango = fruits.index("mango") # Finds the index of an item
count_mango = fruits.count("mango")    # Counts how many times it appears
print(f"Index of 'mango': {index_of_mango} | Count: {count_mango}")

# 4. Ordering & Sorting
fruits.sort()                    # Sorts alphabetically (A-Z)
print(f"Sorted (A-Z): {fruits}")
fruits.reverse()                 # Reverses the current order
print(f"Reversed: {fruits}")

# 5. Copying
fruits_copy = fruits.copy()      # Creates a separate copy of the list
print(f"Copy Created: {fruits_copy}")

# 6. Built-in Functions (Works on lists)
nums = [10, 50, 20, 40]
print(f"Numbers List: {nums}")
print(f"Length: {len(nums)} | Max: {max(nums)} | Min: {min(nums)} | Sum: {sum(nums)}")