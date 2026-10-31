from QuickMart_Functions import *
# quickmart_billing.py - QuickMart Billing System
cart = [
    {"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
    {"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
    {"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
    {"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
    {"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]

print("Task1: Line Total\n", line_total(cart[0]))

print("\nTask2: SubTotal\n", subtotal(cart))

print(f"\nTask3: Discount\n{apply_discount(500)}\n{apply_discount(500, 10)}")

print(f"\nTask 4: GST\n{gst(100)}\n{gst(100, 5)}")

print("\nTask 5: Category Totals")
category_totals(cart)

print(f"\nTask 6: Top items")
top_items(cart)
top_items(cart, 3)

print("\nTask 7:Bill")
print_bill(cart)
