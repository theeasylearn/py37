#write a program to calculate sum and average of all the numbers in list 
list = [10,20,30,40,50,60,100,200,400]
total = 0
count = 0
for number in list:
    print(number)
    total = total + number
    count = count + 1

print("total of whole list",total)
average = total / len(list)
print(f"Average = {average:.2f}",)
# task 
# findout total team score and lowest score and player