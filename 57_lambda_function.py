interest = lambda amount,rate,year: (amount * rate * year) / 100
square = lambda number: number * number 
area = lambda length, width : length * width 

amount = float(input("Enter amount: "))
rate = float(input("Enter rate: "))
year = int(input("Enter number of years: "))

number = int(input("Enter a number: "))

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Simple interest",interest(amount,rate,year))
print("Square ",square(number))
print("area ",area(length,width))