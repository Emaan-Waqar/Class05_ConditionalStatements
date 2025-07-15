cost_price= float(input("Enter the Actual price of the product: "))
selling_price= float(input("Enter the selling price of the product: "))

if selling_price >cost_price:
    amount= selling_price- cost_price
    print("Total profit= {0}".format(amount))
else:
    print("No profit!!")