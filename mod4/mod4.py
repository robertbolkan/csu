# Online Shopping Cart Pseudocode
# Start
#
# Define ItemToPurchase class
#   Attributes:
#       item_name (string)
#       item_price (float)
#       item_quantity (int)
#
#   Default constructor:
#       Set item_name = "none"
#       Set item_price = 0
#       Set item_quantity = 0
#
#   Method print_item_cost():
#       Set item_total = item_price * item_quantity
#       Display: item_name, item_quantity, "@", "$item_price", "=", "$item_total"
#
# Display "Item 1"
# Display "Enter the item name:"
# Get item1_name from the user
# Display "Enter the item price:"
# Get item1_price from the user
# Display "Enter the item quantity:"
# Get item1_quantity from the user
#
# Create item1 as an ItemToPurchase object
# Set item1.item_name = item1_name
# Set item1.item_price = item1_price
# Set item1.item_quantity = item1_quantity
#
# Display "Item 2"
# Repeat the same steps for item2
#
# Set total_cost = (item1.item_price * item1.item_quantity)
#                  + (item2.item_price * item2.item_quantity)
#
# Display "TOTAL COST"
# Call item1.print_item_cost()
# Call item2.print_item_cost()
# Display "Total: $" and total_cost
#
# End


# Define ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        # Default values
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        # Cast to int for clean output like "$1" and "$10" in the example
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(item_total)}")




# Get item 1 information
print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

print()  # Blank line between items.

# Get item 2 information
print("Item 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

print()  # Blank line before total cost output.

# Calculate total cost
total_cost = (item1.item_price * item1.item_quantity) + \
             (item2.item_price * item2.item_quantity)

# Display item costs and total
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${int(total_cost)}")


