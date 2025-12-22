# Mod4 Code: ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        # Default values
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        # Calculate total cost for this item
        item_total = self.item_price * self.item_quantity
        # Display item cost line
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${item_total}")

    def print_item_description(self):
        # Display item description
        print(f"{self.item_name}: {self.item_description}")


# Step 4: ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Set customer name
        self.customer_name = customer_name
        # Set current date
        self.current_date = current_date
        # Create empty list for cart items
        self.cart_items = []

    def add_item(self, item_to_purchase):
        # Add item object to cart
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name != item_to_purchase.item_name:
                continue

            if item_to_purchase.item_description != "none":
                item.item_description = item_to_purchase.item_description
            if item_to_purchase.item_price != 0:
                item.item_price = item_to_purchase.item_price
            if item_to_purchase.item_quantity != 0:
                item.item_quantity = item_to_purchase.item_quantity
            return

        print("Item not found in cart. Nothing modified.")


    # Get item count in cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Sum total costs across all items
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        # Print header lines
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        # Print message if cart is empty
        if len(self.cart_items) == 0:
            print()
            print("SHOPPING CART IS EMPTY")
            print()
            print("Total: $0")
            return

        # Print each item cost line
        for item in self.cart_items:
            item.print_item_cost()

        # Print total line
        print()
        print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        # Print header lines
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        # Print each item description line
        for item in self.cart_items:
            item.print_item_description()


# Step 5: Implement print_menu(cart)
# Output menu options. Continue until user enters 'q'

def print_menu(cart):
    # Set initial choice (loop runs until 'q')
    choice = ""

    while choice != "q":
        # Display menu
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        # Get user choice
        choice = input("Choose an option:\n")
        print()

        # Add item option
        if choice == "a":
            print("ADD ITEM TO CART")
            # Create a new item object
            item = ItemToPurchase()
            # Get item fields
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = int(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            print()
            # Add item to cart
            cart.add_item(item)

        # Remove item option
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            # Get item name to remove
            name = input("Enter name of item to remove:\n")
            print()
            # Remove item
            cart.remove_item(name)

        # Change item quantity option
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            # Build an item object with name + new quantity
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_quantity = int(input("Enter the new quantity:\n"))
            print()
            # Modify item in cart
            cart.modify_item(item)

        # Step 6: Output shopping cart option
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            # Print cart totals
            cart.print_total()
            print()

        # Step 6: Output items' descriptions option
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            # Print item descriptions
            cart.print_descriptions()
            print()

        # Quit option
        elif choice == "q":
            pass

        # Invalid option, keep prompting
        else:
            continue


# main(): create cart + call print_menu()
def main():
    # Get customer name and date
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    # Echo inputs (common in assignment examples)
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()

    # Create shopping cart object
    cart = ShoppingCart(customer_name, current_date)
    # Start menu loop
    print_menu(cart)


# Run main
if __name__ == "__main__":
    main()
