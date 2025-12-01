# Part 1 – Meal Total with Tip and Tax Pseudocode
# Start
#
# Display: "Enter the charge for the food:"
# Get food_charge from the user
#
# Set tip_rate = 0.18
# Set tax_rate = 0.07
#
# Set tip_amount = food_charge * tip_rate
# Set tax_amount = food_charge * tax_rate
# Set total_amount = food_charge + tip_amount + tax_amount
#
# Display "Food charge:" and food_charge
# Display "Tip amount:" and tip_amount
# Display "Tax amount:" and tax_amount
# Display "Total amount:" and total_amount
#
# End

# Ask the user for the cost of the food.
food_charge = float(input("Enter the charge for the food: "))

# Tip and tax rates.
tip_rate = 0.18
tax_rate = 0.07

# Calculate tip and tax.
tip_amount = food_charge * tip_rate
tax_amount = food_charge * tax_rate

# Calculate total.
total_amount = food_charge + tip_amount + tax_amount

# Display each amount.
print("Food charge:", food_charge)
print("Tip amount (18%):", tip_amount)
print("Tax amount (7%):", tax_amount)
print("Total amount:", total_amount)


# Part 2 – 24-Hour Clock Alarm Pseudocode
# Start
#
# Display: "Enter the current time (0–23):"
# Get current_time from the user
#
# Display: "Enter the number of hours to wait for the alarm:"
# Get hours_to_wait from the user
#
# Set alarm_time = (current_time + hours_to_wait) % 24
#
# Display "The alarm will go off at:" and alarm_time
#
# End

# Ask the user for the current time (0–23).
current_time = int(input("Enter the current time (0–23): "))

# Ask how many hours to wait.
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off.
alarm_time = (current_time + hours_to_wait) % 24

# Display the alarm time.
print("The alarm will go off at:", alarm_time)