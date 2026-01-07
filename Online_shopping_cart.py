class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.pid} | {self.name} | ₹{self.price}")


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    def remove_product(self, pid):
        for item in self.items:
            if item.pid == pid:
                self.items.remove(item)
                print(f"{item.name} removed from cart")
                return
        print("Product not found")

    def show_cart(self):
        if not self.items:
            print("Cart is empty")
            return

        print("\nItems in Cart:")
        for item in self.items:
            item.display()

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        print(f"\nTotal Amount: ₹{total}")


# ---- Main Program ----
p1 = Product(1, "Laptop", 55000)
p2 = Product(2, "Mouse", 500)
p3 = Product(3, "Keyboard", 1200)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.show_cart()
cart.calculate_total()

cart.remove_product(2)
cart.show_cart()
cart.calculate_total()
