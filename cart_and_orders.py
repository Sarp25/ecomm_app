import datetime
from storage import load_json, save_json

ORDER_FILE= "orders.json"

class ShoppingCart:
    def __init__(self):
        self.contents = []

    def add_to_bag(self, product, amount):
        if amount<= 0:
            return False, "You have to add at least 1 item!"

        for item in self.contents:
            if item["product_id"]==product["product_id"]:
                item["qty"] +=amount
                return True, f"Updated {product['name']} quantity."

        self.contents.append({
            "product_id": product["product_id"],
            "name": product["name"],
            "unit_price": product["price"],
            "qty": amount
        })
        return True, f"Added {product['name']} to your bag."

    def remove_from_bag(self, p_id, amount_to_remove=None):
        for item in self.contents:
            if item["product_id"] == p_id:
                if amount_to_remove is None or amount_to_remove >= item["qty"]:
                    self.contents.remove(item)
                else:
                    item["qty"] -=amount_to_remove
                return True, "Bag updated!"
        return False, "We couldn't find that item in your bag."

    def empty_bag(self):
        self.contents.clear()

    def calculate_total(self):
        total_sum= 0
        for item in self.contents:
            total_sum +=item["unit_price"]*item["qty"]
        return total_sum

    def show_bag_contents(self):
        if not self.contents:
            print("\nYour shopping bag is currently empty.")
            return

        print(f"\n{'Item Name':<20} {'Qty':<5} {'Price':<10} {'Subtotal':<10}")
        print("~" * 50)

        for item in self.contents:
            sub= item["unit_price"]*item["qty"]
            print(f"{item['name']:<20} {item['qty']:<5} ${item['unit_price']:<9.2f} ${sub:<9.2f}")

        print("~" * 50)
        print(f"Grand Total: ${self.calculate_total():.2f}")


class OrderManager:
    """Handles saving the orders to the json file permanently"""
    def __init__(self):
        self.past_orders=load_json(ORDER_FILE, [])

    def record_new_order(self, buyer_name, items_list, final_price):
        now= datetime.datetime.now()
        new_id= f"ORDER-{now.strftime('%y%m%d-%H%M%S')}"

        receipt= {
            "order_id": new_id,
            "username": buyer_name,
            "items": items_list,
            "total": round(final_price, 2),
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
        }

        self.past_orders.append(receipt)
        save_json(ORDER_FILE, self.past_orders)
        
        return new_id
    
    def get_orders_for_user(self, username):
        return [o for o in self.past_orders if o["username"]== username]