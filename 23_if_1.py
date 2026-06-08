#write a program to figure out profit or loss amount from given purchase and sales price. 
purchase_price = float(input("Enter product purchase price"))
sales_price = float(input("Enter product sales price"))

#process 
difference = sales_price - purchase_price 

if difference>0: #< > <= >=
    print("you have made profit of ",difference)

if difference<0: 
    print("you have made loss of ",difference)

print("Good bye.")
