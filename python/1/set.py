# 1. Basics: Creating and Adding/Removing
s1 = {1, 2, 3, 4, 5}
s1.add(6)
s1.discard(10)      # Safe: No error even though 10 isn't there
s1.remove(1)        # Will error if 1 isn't there
popped = s1.pop()   # Removes a RANDOM item
print(f"Basic Set: {s1} | Popped Item: {popped}")

# 2. Mathematical Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (All items from both)
print(f"Union: {A.union(B)}")              # Or A | B

# Intersection (Only common items)
print(f"Intersection: {A.intersection(B)}") # Or A & B

# Difference (Items in A but NOT in B)
print(f"Difference: {A.difference(B)}")     # Or A - B

# Symmetric Difference (Items in EITHER A or B, but NOT both)
print(f"Symmetric Diff: {A.symmetric_difference(B)}") # Or A ^ B

# 3. Validation / Boolean Methods
small = {3, 4}
print(f"Is subset? {small.issubset(A)}")    # True
print(f"Are disjoint? {A.isdisjoint({9})}") # True (No common items)

# 4. In-Place Updates (Modifies the original set)
A.intersection_update(B) 
print(f"A after intersection_update: {A}") # A is now {3, 4}