# Average Rainfall Pseudocode
# Start
#
# Display "Enter the number of years:"
# Get years from the user
#
# Set total_rainfall = 0
# Set total_months = years * 12
#
# For each year from 1 to years
#   For each month from 1 to 12
#       Display prompt for rainfall for that year/month
#       Get rainfall from the user
#       Add rainfall to total_rainfall
#
# Set average_rainfall = total_rainfall / total_months
#
# Display total_months
# Display total_rainfall
# Display average_rainfall
#
# End


# Average Rainfall

# Get years from the user
years = int(input("Enter the number of years: "))

# Initialize total_rainfall and total_months
total_rainfall = 0.0
total_months = years * 12

# Loop over each month of each year
for year in range(1, years + 1):
    for month in range(1, 13):
        
        # Get rainfall from the user for this month and year
        rainfall = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))
        total_rainfall += rainfall

# Calculate average rainfall per month
average_rainfall = total_rainfall / total_months

# Print results
print(f"Total inches of rainfall: {total_rainfall} in {total_months} months")
print(f"Average rainfall per month: {average_rainfall}")




# Book Club Points Pseudocode
# Start
#
# Display "Enter the number of books purchased this month:"
# Get books_purchased from the user
#
# If books_purchased is 0 or 1
#   Set points = 0
# Else if books_purchased is 2 or 3
#   Set points = 5
# Else if books_purchased is 4 or 5
#   Set points = 15
# Else if books_purchased is 6 or 7
#   Set points = 30
# Else
#   Set points = 60
#
# Display points
#
# End


# Book Club Points

# Get books_purchased from the user
books_purchased = int(input("Enter the number of books purchased this month: "))

# Calculate points
if books_purchased <= 1:
    points = 0
elif books_purchased <= 3:
    points = 5
elif books_purchased <= 5:
    points = 15
elif books_purchased <= 7:
    points = 30
else:
    points = 60

# Print the points
print(f"Points awarded: {points}")


