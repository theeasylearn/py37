#write a program to figure how many days given month has 
# input : month = 1 output : this month has 31 days 
# input : month = 2 output : this month has 28 days 
# input : month = 4 output : this month has 30 days 
# input : month = 12 output : this month has 31 days 
# `[1, 3, 5, 7, 8, 10, 12]` has 31 days
month = int(input("Enter month between 1 to 12"))

if month<1 or month>12:
    print("invalid month")
else:
    if month == 2:
        print("this month has 28 days")
        exit(1) #code execute stop here 
        
    #we must join multiple reltional expression using logical operator and / or 
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12: 
        print("this month has 31 days")
    else:
        print("this month has 30 days")

print("good bye")