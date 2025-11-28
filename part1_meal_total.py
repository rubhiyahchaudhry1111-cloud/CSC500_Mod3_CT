# Part 1: Meal Total Calculator

# Ask user for food charge
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07

# Store components in a list of (label, amount) tuples
components = [
    ("Food charge", food_charge),
    ("Tip (18%)", tip),
    ("Sales Tax (7%)", tax)
]

# Use a loop to display each amount and calculate total
total = 0
for label, amount in components:
    print(f"{label}: ${amount:.2f}")
    total += amount

# Display total
print(f"Total Price: ${total:.2f}")
