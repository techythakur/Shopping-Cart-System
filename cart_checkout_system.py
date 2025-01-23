from collections import Counter

class Product:
    """
    Represents a product in the system.

    Attributes:
        name (str): The name of the product.
        individual_price (int): The price of a single unit of the product.
        offer_count (int, optional): The number of items required to qualify for an offer.
        offer_price (int, optional): The discounted price for the offer count.
    """
    def __init__(self, name, individual_price, offer_count=None, offer_price=None):
        self.name = name
        self.individual_price = individual_price
        self.offer_count = offer_count
        self.offer_price = offer_price

    def calculate_price(self, quantity):
        """
        Calculates the total price for a given quantity, applying offers if applicable.
        """
        if self.offer_count:
            offer_sets = quantity // self.offer_count
            remaining_items = quantity % self.offer_count
            total_price = offer_sets * self.offer_price + remaining_items * self.individual_price
            return total_price
        else:
            return quantity * self.individual_price
    
    def get_details(self):
        """
        Returns product details including pricing and offers if any.
        """
        if self.offer_count:
            return f"Name: {self.name}, Price: {self.individual_price}, Offer: {self.offer_count} for {self.offer_price}"
        else:
            return f"Name: {self.name}, Price: {self.individual_price}, No offer available"

class Cart:
    """
    Represents a cart holding items selected by the user.
    """
    def __init__(self):
        self.items = Counter()

    def add_items(self, item):
        """
        Adds items to the cart.
        """
        self.items.update(item)
        print(f"\nAdded {''.join(item)} to the cart.")
    
    def view_cart(self):
        """
        Displays the items in the cart.
        """
        if not self.items:
            print("\nYour cart is empty.")
        else:
            print("\nItems in your cart:")
            for item, quantity in self.items.items():
                print(f"Item: {item}, Quantity: {quantity}")
    
    def clear_cart(self):
        """
        Removes all items from the cart.
        """
        self.items.clear()
        print("\nYour cart has been cleared.")

    def calculate_total(self, products):
        """
        Calculates the total price of items in the cart based on the products.
        """
        total_price = 0
        for item, quantity in self.items.items():
            product = products[item]
            total_price += product.calculate_price(quantity)
        return total_price

class CheckoutSystem:
    """
    Represents the main checkout system managing products and the shopping cart.
    """
    def __init__(self):
        self.products = {
            'A': Product('A', 50, 3, 130),
            'B': Product('B', 30, 2, 45),
            'C': Product('C', 20),
            'D': Product('D', 15)
        }
        print("Default Product Details Loaded.")
        self.cart = Cart()

    def add_or_update_product(self, name, individual_price, offer_count=None, offer_price=None):
        """
        Adds a new product or updates an existing product.
        """
        if name in self.products:
            existing_product = self.products[name]
            existing_product.individual_price = individual_price
            existing_product.offer_count = offer_count
            existing_product.offer_price = offer_price
            print(f"\nUpdated Product '{name}' details.")
        else:
            self.products[name] = Product(name, individual_price, offer_count, offer_price)
            print(f"\nAdded new Product '{name}'.")

    def scan_items(self, item_list):
        """
        Adds items to the cart, ignoring invalid items not present in the products catalog.
        """
        valid_items = [item for item in item_list if item in self.products]
        invalid_items = [item for item in item_list if item not in self.products]

        if invalid_items:
            print(f"\nInvalid items detected and ignored: {', '.join(invalid_items)}")
        
        if valid_items:
            self.cart.add_items(valid_items)

    def calculate_total_price(self):
        """
        Calculates the total price of items in the cart.
        """
        total_price = self.cart.calculate_total(self.products)
        return total_price

    def list_products(self):
        """
        Lists all products with their details.
        """
        if not self.products:
            print("\nNo products available.")
        else:
            print("\nAvailable Products:")
            for product in self.products.values():
                print(product.get_details())    


def run_checkout_system():
    """
    Main function to run the checkout system in an interactive mode.
    """
    checkout_system = CheckoutSystem()
    while True:
        print("\nChoose an option:")
        print("1. List All Products.")
        print("2. Add/Update any Product.")
        print("3. Add Items to Cart.")
        print("4. View Items in Cart.")
        print("5. Clear Cart.")
        print("6. View Total Price")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            checkout_system.list_products()
            
        elif choice == "2":
            name = input("Enter Product Name: ").strip().upper()
            individual_price = int(input("Enter Individual Price: "))
            offer_count = input("Enter Quantity for Offer (or press Enter to skip): ").strip()
            offer_price = input("Enter Offer Price (or press Enter to skip): ").strip()
            offer_count = int(offer_count) if offer_count else None
            offer_price = int(offer_price) if offer_price else None
            checkout_system.add_or_update_product(name, individual_price, offer_count, offer_price)

        elif choice == "3":
            items = input("Enter Items to Add to Cart (e.g., ABABACC): ").strip().upper()
            checkout_system.scan_items(items)

        elif choice == "4":
            checkout_system.cart.view_cart()
            
        elif choice == "5":
            checkout_system.cart.clear_cart()
            
        elif choice == "6":
            total_price = checkout_system.calculate_total_price()
            print(f"\nTotal Price: {total_price}")
            
        elif choice == "7":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-7).")


if __name__ == "__main__":
    run_checkout_system()
