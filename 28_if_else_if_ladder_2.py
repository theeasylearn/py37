#write a program to accept month number of year from user. and display how many days it has in that month
# month = 1 then display 31 days
# month = 2 then display 28/29
# month = 3 then display 31 days
# month = 12 then display output 31
# otherwise display invalid month
#  month 1, 3, 5, 7, 8, 10, 12 has 31 days 
#  month 4,6,9,11 has 30 days 
#  month 2 has 29 days 
month = int(input("Enter month of year (must be between 1 to 12)"))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("this month has 31 days")
elif month==4 or month==6 or month==9 or month==11:
    print("this month has 30 days")
elif month==2:
    print("this month has 28/29 days")
else:
    print("it is not valid month")

            