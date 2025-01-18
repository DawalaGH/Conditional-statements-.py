actual_cost=int(input("enter cost:"))
sale_amount=int(input("enter sale:"))

if(sale_amount>actual_cost):
     amount = sale_amount-actual_cost

     print("profit is= {0}".format(amount))

else:
     print("no profit")