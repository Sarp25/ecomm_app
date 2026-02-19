from storage import load_json, save_json

PRODUCTS_FILE= "products.json"

class ProductManager:

    def __init__(self):
        self.inventory= load_json(PRODUCTS_FILE, [])

    def save_inventory(self):
        save_json(PRODUCTS_FILE, self.inventory)

    def list_products(self):
        return self.inventory

    def get_product(self, product_id):
        for p in self.inventory:
            if p["product_id"]== product_id:
                return p
        return None

    def search_products(self, keyword):
        kw= keyword.lower()
        return [p for p in self.inventory if kw in p["name"].lower()]

    def update_stock(self, product_id, delta):
        product =self.get_product(product_id)
        if not product:
            return False

        product["stock"] =max(0, product.get("stock", 0)+ delta)
        self.save_inventory()
        return True