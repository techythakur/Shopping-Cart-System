# Agrichain Cart Checkout System

This is a Python-based Cart checkout system that allows users to:
1. Add or update products with pricing and offers.
2. Add items to a cart for purchase.
3. View items in the cart.
4. Clear the cart.
5. Calculate the total price of items in the cart.
6. View all available products and their details.

The program offers interactive and default product initialization modes and supports continuous user interaction through a menu-driven interface.

---

## Features

1. **List All Products**
   - View all products in the system with their prices and offers (if any).
   - Example Output:
     ```
     Available Products:
     Name: A, Price: 50, Offer: 3 for 130
     Name: B, Price: 30, Offer: 2 for 45
     Name: C, Price: 20, No offer available
     Name: D, Price: 15, No offer available
     ```

2. **Add/Update Products**
   - Add new products to the system or update existing product details, including offers.
   - Example Interaction:
     ```
     Enter Product Name: E
     Enter Individual Price: 10
     Enter Quantity for Offer (or press Enter to skip): 2
     Enter Offer Price (or press Enter to skip): 15
     Added new Product 'E'.
     ```

3. **Add Items to Cart**
   - Add items to the cart by entering them as a single string (e.g., `AAAABBCC`).
   - Invalid items are ignored.
   - Example Interaction:
     ```
     Enter Items to Add to Cart (or press Enter to stop): AAAABBCC
     Added AAAABBCC to the cart.
     Enter Items to Add to Cart (or press Enter to stop): 4
     Invalid items detected and ignored: 4
     ```

4. **View Items in Cart**
   - Displays the items in the cart with their respective quantities.
   - Example Output:
     ```
     Items in your cart:
     Item: A, Quantity: 4
     Item: B, Quantity: 2
     Item: C, Quantity: 2
     ```

5. **Clear Cart**
   - Clears all items in the cart.
   - Example Output:
     ```
     Your cart has been cleared.
     ```

6. **View Total Price**
   - Calculates and displays the total price of all items in the cart, applying applicable discounts.
   - Example Output:
     ```
     Total Price: 265
     ```

7. **Exit**
   - Exits the program.

---

## How to Run

1. Clone or download this repository.
2. Run the script using Python 3:
   ```bash
   python3 cart_checkout_system.py
