plant_name = "Spekboom"  # string
quantity = 45  # int
unit_price = 35.00  # float
in_stock = True  # boolean
plant_list = ["Spekboom", "Aloe Vera", "Fever Tree", "Plumbago"]  # list
price_dict = {"Spekboom": 35.00, "Aloe Vera": 28.50}  # dictionary
supplier_set = {"KZN Indigenous Growers", "Green Thumb Wholesalers"}  # set

print("Plant name:", plant_name)
print("Quantity in stock:", quantity)
print("Unit price:", unit_price)
print("In stock:", in_stock)
print("Plant list:", plant_list)
print("Price dictionary:", price_dict)
print("Supplier set:", supplier_set)

total_value = quantity * unit_price
print("Total stock value:", total_value)

reorder_level = 10
if quantity < reorder_level:
    print("Stock is below the reorder level.")
else:
    print("Stock is above the reorder level.")