# --- 1. Writing to a File ('w') ---
# This will create 'test.txt' or overwrite it if it exists
with open("test.txt", "w") as f:
    f.write("Line 1: Hello Python!\n")
    f.writelines(["Line 2: Learning Files\n", "Line 3: File Handling is easy\n"])

# --- 2. Reading from a File ('r') ---
print("--- Reading Full Content ---")
with open("test.txt", "r") as f:
    content = f.read() # Reads the entire file as one string
    print(content)

# --- 3. Reading Line by Line ---
print("--- Reading Line by Line ---")
with open("test.txt", "r") as f:
    # Use a loop to read one line at a time (memory efficient)
    for line in f:
        print(f"Data: {line.strip()}")

# --- 4. Appending Data ('a') ---
# This adds data to the bottom without deleting the top
with open("test.txt", "a") as f:
    f.write("Line 4: This was added later.\n")

# --- 5. Advanced: Seek and Tell ---
print("\n--- Using Seek and Tell ---")
with open("test.txt", "r") as f:
    print(f"Initial Cursor Position: {f.tell()}") 
    f.read(5) # Read first 5 characters
    print(f"Position after reading 5 chars: {f.tell()}")
    
    f.seek(0) # Move cursor back to the very beginning
    print(f"Back at the start: {f.readline()}")

# --- 6. Checking File Properties ---
f = open("test.txt", "r")
print(f"\nFile Name: {f.name}")
print(f"Is Closed? {f.closed}")
f.close() # Manual close needed since 'with' wasn't used here
print(f"Is Closed now? {f.closed}")