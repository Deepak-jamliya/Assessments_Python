def product(name, price, category):
    print("\nProduct Details Displayed Successfully")
    print("Product Name :", name)
    print("Price        :", price)
    print("Category     :", category)

def products(*prices):
    total = sum(prices)
    print("\nTotal Bill Amount :", total)