# --- 1. DATA INITIALIZATION ---
# String with escape characters
raw_data = "  ahmad\tnawaz\n" 
# List of numbers
scores = [85, 92, 78, 92, 88]
# Tuple (Immutable constants)
version_info = (3, 10, "Stable")
# Dictionary (Key-Value pairs)
user_profile = {"id": 101, "status": "active"}

# --- 2. STRING & LIST PROCESSING ---
# Clean the string and split into a list
clean_name = raw_data.strip().title()
name_parts = clean_name.split() # ['Ahmad', 'Nawaz']

# Add items to list and remove duplicates using a SET
scores.append(95)
unique_scores = sorted(list(set(scores)), reverse=True)

# --- 3. DICTIONARY UPDATE ---
user_profile.update({
    "full_name": clean_name,
    "top_score": unique_scores[0],
    "all_scores": unique_scores
})

# --- 4. CONDITIONAL LOGIC & LOOPS (ALL IN ONE) ---
print(f"--- Processing Profile: {user_profile['full_name']} ---")

# Loop through Dictionary Items
for key, value in user_profile.items():
    
    # Conditional logic based on Data Types
    if isinstance(value, list):
        print(f"{key.upper()}:")
        for item in value:
            # Loop control: skip if score is below 80
            if item < 80:
                continue
            print(f"  > Passing Score: {item}")
            
    elif isinstance(value, int):
        if value > 90:
            print(f"{key.upper()}: {value} (Excellent!)")
        else:
            print(f"{key.upper()}: {value}")
            
    else:
        print(f"{key.upper()}: {value}")

# --- 5. WHILE LOOP & TERNARY OPERATOR ---
attempts = 3
while attempts > 0:
    access = "Granted" if user_profile["status"] == "active" else "Denied"
    print(f"\nSystem Access: {access} (Session expires in {attempts} hours)")
    break # Using break to prevent infinite loop for this demo

print("\n--- Process Complete ---")