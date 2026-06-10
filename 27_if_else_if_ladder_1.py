'''
#write a program to accept day of week from user. and display name of the day 
# day = 1 then display output monday
# day = 2 then display output tuesday
# day = 3 then display output wednesday
# day = 8 then display invalid day 
'''
day = int(input("Enter day of week (must be between 1 to 7)"))

if day==1:
    print("it is monday")
elif day==2:
    print("it is tuesday")
elif day==3:
    print("it is wednesday")
elif day==4:
    print("it is thursday")
elif day==5:
    print("it is friday")
elif day==6:
    print("it is saturday")
elif day==7:
    print("it is sunday")
else:
    print("it is not valid day of week")
