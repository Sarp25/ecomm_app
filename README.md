# Star Shopping
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
![Release Version](https://img.shields.io/badge/Version-1.0.0-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

This is a **Python command-line shopping application** that simulates a basic e-commerce system.
Users can register, log in, browse products, manage a shopping cart, place orders, and view their order history.

---

## How to Run the Program

### Requirements

* Python **3.8 or higher**
* All project files in the same directory

### Steps

1. Open a terminal in the project folder
2. Run the main program using:

```bash
python main.py
```

3. Follow the on-screen menu instructions to:

   * Register or log in
   * Browse products
   * Add items to the shopping cart
   * Checkout and view order history

---

## Features Implemented

### User Management

* User registration with username and password
* Password length validation
* Secure login using hashed passwords
* Persistent user data storage

### Product Management

* Load products from a JSON file
* Browse all products
* Search products by keyword
* Track and update stock quantities

### Shopping Cart

* Session-based shopping cart
* Add items to cart
* Remove items or reduce quantities
* View cart contents in receipt-style format
* Automatic total price calculation

### Order Management

* Checkout system that creates permanent orders
* Unique order IDs generated using timestamps
* Order history stored and retrievable per user
* Product stock updated after checkout

### User Interface

* Text-based terminal menus
* Input validation and error handling
* Animated text output for improved user experience

---

## How Data Is Stored

* Data is stored using **JSON files** for simplicity and persistence:

  * `users.json` → Registered users
  * `products.json` → Product inventory
  * `orders.json` → Completed orders

* Data handling is abstracted using helper functions:

  * `load_json()` safely loads data
  * `save_json()` writes data back to files

* During program execution:

  * Data is loaded into memory for faster access
  * Files are updated only when changes occur

---

## Known Limitations

* JSON files are not suitable for large-scale or concurrent use
* Shopping cart is **session-based** and resets on logout
* No admin interface for managing products
* No database or web interface (terminal-only application)

---

### Author

Sarp Baran Yıldız
