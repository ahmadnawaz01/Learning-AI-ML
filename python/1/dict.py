# Setup initial dictionary
user = {"id": 101, "name": "Ahmad", "role": "Admin"}

# 1. keys(), values(), items() - The "View" methods
print(f"Keys:   {user.keys()}")
print(f"Values: {user.values()}")
print(f"Items:  {user.items()}")

# 2. get() - The safe access method
# Doesn't crash if "email" is missing, returns "Not Found" instead
print(f"Email:  {user.get('email', 'Not Found')}")

# 3. setdefault() - Get if exists, set if not
# "country" isn't there, so it adds "Pakistan"
country = user.setdefault("country", "Pakistan")
print(f"SetDefault: {user}")

# 4. update() - Merging or changing multiple values
user.update({"role": "SuperAdmin", "status": "Active"})
print(f"After Update: {user}")

# 5. fromkeys() - Create a NEW dict from a list
# Note: This is a Class Method (called on 'dict')
new_keys = ['task1', 'task2', 'task3']
tasks = dict.fromkeys(new_keys, "Pending")
print(f"FromKeys: {tasks}")

# 6. pop() - Remove by key
removed_val = user.pop("id")
print(f"Popped 'id': {removed_val} | Current Dict: {user}")

# 7. popitem() - Remove last item
last_pair = user.popitem()
print(f"PopItem: {last_pair} | Current Dict: {user}")

# 8. copy() - Duplicate the dict
user_backup = user.copy()

# 9. clear() - Empty the dict
user.clear()
print(f"After Clear: {user}")
print(f"Backup still exists: {user_backup}")