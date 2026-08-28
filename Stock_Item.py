class StockItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def describe(self):
        print(f"{self.name}: {self.quantity} units at R{self.price} each.")


item = StockItem("Spekboom", 45, 35.00)
item.describe()

with open("stock_notes.txt", "w") as f:
    f.write("Spekboom stock at the Pinetown branch is currently 45 units, supplied by KZN Indigenous Growers.")

with open("stock_notes.txt", "r") as f:
    print(f.read())

try:
    entered_quantity = int(input("Enter the new stock quantity: "))
    print("Quantity updated to:", entered_quantity)
except ValueError:
    print("Please enter a valid number.")