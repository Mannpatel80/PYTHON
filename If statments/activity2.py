actual_cost=float(input( " Please Enter the Actual Product Price: "))
sales_cost=float(input( " Please Enter the Sales Amount :"))

if( sales_cost>actual_cost):
    amount=sales_cost-actual_cost
    print("Total Profit={0}".format(amount))
else:
    print("no profit:(")
