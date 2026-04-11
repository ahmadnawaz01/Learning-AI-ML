# The original string (with extra spaces for demonstration)
a = " ahmad nawaz "

print(f"Original: '{a}'")
print("-" * 30)

# 1. Measurement & Search
print(f"Length:          {len(a)}")             # Total characters (13)
print(f"Ends with 'az ': {a.endswith('az ')}")   # True
print(f"Starts with 'a': {a.startswith('a')}")    # False (starts with a space!)
print(f"Count 'a':       {a.count('a')}")        # 3

# 2. Cleaning (Crucial for user input)
stripped = a.strip()
print(f"Stripped:       '{stripped}'")          # Removes leading/trailing spaces

# 3. Case Transformation (Using the cleaned version)
print(f"Capitalize:      {stripped.capitalize()}") # Ahmad nawaz
print(f"Title Case:      {stripped.title()}")      # Ahmad Nawaz
print(f"Upper Case:      {stripped.upper()}")      # AHMAD NAWAZ

# 4. Replacement & Splitting
print(f"Replace:         {stripped.replace('ahmad', 'ali')}") # ali nawaz
words = stripped.split() 
print(f"Split into List: {words}")               # ['ahmad', 'nawaz']

# 5. Joining (Turning a list back into a string)
print(f"Joined with '-': {'-'.join(words)}")      # ahmad-nawaz

# 6. Validation
print(f"Is Alphabetic?   {stripped.isalpha()}")  # False (because of the space)
print(f"Is Digit?        {stripped.isdigit()}")  # False