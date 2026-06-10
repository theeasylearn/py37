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
list31 = [1, 3, 5, 7, 8, 10, 12]
list30 = [4,6,9,11]

if month in list31:
    print("this month has 31 days")
elif month in list30:
    print("this month has 30 days")
elif month==2:
    print("this month has 28/29 days")
else:
    print("it is not valid month")

            