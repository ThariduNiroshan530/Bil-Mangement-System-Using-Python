import datetime


class Bill:
    def __init__(self):
        self.products = []
        self.time = datetime.datetime.now()

    def add_product(self, product_name, price, quantity, discount=0):
        product = {
            'product_name': product_name,
            'price': price,
            'quantity': quantity,
            'discount': discount
        }
        self.products.append(product)

    def calculate_total_cost(self):
        total_cost = 0
        for product in self.products:
            discounted_price = product['price'] * \
                (1 - product['discount'] / 100)
            total_cost += discounted_price * product['quantity']
        return total_cost

    def calculate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product['price']
        return total_price

    def get_bill_details(self):
        total_cost = self.calculate_total_cost()
        total_price = self.calculate_total_price()

        print("\n-------- Bill --------")
        for product in self.products:
            discounted_price = product['price'] * \
                (1 - product['discount'] / 100)
            print(f"Product Name: {product['product_name']}")
            print(f"Price Per Unit: Rs{product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            print(f"Discount: {product['discount']}%")
            print(f"Discounted Price: Rs{discounted_price:.2f}")
            print("----------------------")

        print(f"\nTotal Price: Rs{total_price:.2f}")
        print(f"Total Cost: Rs{total_cost:.2f}\nTime: {self.time}")


bill = Bill()

while True:
    print("\n--- Bill Management System ---")
    print("1. Add Product")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the price: "))
        discount = float(input("Enter the discount: "))
        quantity = int(input("Enter the quantity: "))

        bill.add_product(product_name, price, quantity, discount)

    elif choice == "2":
        bill.get_bill_details()

    elif choice == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
