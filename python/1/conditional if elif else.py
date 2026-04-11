# 1. Get input (simulated for this example)
age = 18
has_membership = True

# 2. Start the Conditional Logic
if age < 0:
    print("Error: Age cannot be negative.")

elif age < 13:
    print("Category: Child Ticket ($5)")

elif age < 18:
    print("Category: Junior Ticket ($10)")

elif age >= 18:
    print("Category: Adult Ticket ($15)")
    
    # 3. Nested Conditional (if inside an if)
    if has_membership:
        print("Special Discount: 20% off applied for members!")
    else:
        print("Tip: Join our membership to save 20%.")

else:
    # This block runs if none of the above are True
    print("Category: General Inquiry Required")

# 4. Short-hand (Ternary Operator)
# A quick way to write an if/else in one line
status = "Eligible to Vote" if age >= 18 else "Too Young to Vote"
print(f"Voting Status: {status}")