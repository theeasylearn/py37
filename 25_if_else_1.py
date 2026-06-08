#write a program figure whether given year is millennium year or not 
# input : 1000 output : it is millennium year
# input : 2026 output : it is not millennium years year 

year = int(input("Enter year "))
reminder = year % 1000
if reminder==0:
    print('it is millennium year')
else:
    print('it is not millennium year')

print("good bye")