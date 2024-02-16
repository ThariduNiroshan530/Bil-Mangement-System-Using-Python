import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Bill:
    def __init__(self):
        self.products = []
        self.time = datetime.now()

    def add_product(self, product_name, price, quantity, discount=0):
        product = {
            'product_name': product_name,
            'price': price,
            'quantity': quantity,
            'discount': discount
        }
        self.products.append(product)

    def remove_product(self, index):
        if 0 <= index < len(self.products):
            self.products.pop(index)

    def calculate_total_cost(self):
        total_cost = 0
        for product in self.products:
            discounted_price = product['price'] * (1 - product['discount'] / 100)
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

        bill_output = "\n-------- Bill --------\n"
        for product in self.products:
            discounted_price = product['price'] * (1 - product['discount'] / 100)
            bill_output += f"Product Name: {product['product_name']}\n"
            bill_output += f"Price Per Unit: Rs{product['price']:.2f}\n"
            bill_output += f"Quantity: {product['quantity']}\n"
            bill_output += f"Discount: {product['discount']}%\n"
            bill_output += f"Discounted Price: Rs{discounted_price:.2f}\n"
            bill_output += "----------------------\n"

        bill_output += f"\nTotal Price: Rs{total_price:.2f}\n"
        bill_output += f"Total Cost: Rs{total_cost:.2f}\nTime: {self.time}"
        return bill_output

class BillManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Management System")

        self.bill = Bill()

        self.product_name_label = tk.Label(root, text="Product Name:")
        self.product_name_label.pack()
        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.pack()

        self.price_label = tk.Label(root, text="Price per unit:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.discount_label = tk.Label(root, text="Discount (%):")
        self.discount_label.pack()
        self.discount_entry = tk.Entry(root)
        self.discount_entry.pack()

        self.add_product_button = tk.Button(root, text="Add Product", command=self.add_product_to_bill)
        self.add_product_button.pack()

        self.remove_product_button = tk.Button(root, text="Remove Product", command=self.remove_product_from_bill)
        self.remove_product_button.pack()

        self.generate_bill_button = tk.Button(root, text="Generate Bill", command=self.generate_bill)
        self.generate_bill_button.pack()

        self.bill_output_label = tk.Label(root, text="Bill Output", font=("bold", 14))
        self.bill_output_label.pack()
        self.bill_output_text = tk.Text(root, width=40, height=10)
        self.bill_output_text.pack()

    def add_product_to_bill(self):
        # Retrieve input values from entry fields
        product_name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        discount = float(self.discount_entry.get())

        # Add the product to the bill
        self.bill.add_product(product_name, price, quantity, discount)

        # Clear input fields
        self.product_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.discount_entry.delete(0, tk.END)

    def remove_product_from_bill(self):
        index = int(tk.simpledialog.askstring("Remove Product", "Enter the index of the product to remove:"))
        if index is not None:
            self.bill.remove_product(index - 1)

    def generate_bill(self):
        bill_output = self.bill.get_bill_details()
        self.bill_output_text.delete(1.0, tk.END)
        self.bill_output_text.insert(tk.END, bill_output)

def main():
    # Create the Tkinter application window
    root = tk.Tk()
    bill_management_app = BillManagementApp(root)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
