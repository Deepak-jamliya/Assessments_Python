def invoice(product_name, price, tax=10):
    tax_amount = price * tax / 100
    final_amount = price + tax_amount
    print("\nInvoice Generated Successfully")
    print("Product Name :", product_name)
    print("Price        :", price)
    print("Tax (%)      :", tax)
    print("Final Amount :", final_amount)