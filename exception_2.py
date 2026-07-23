#write a program to calculate sum and average of all the numbers in list 
# list = ['ball',False,'bat']
list = [10,20,30,'ball',40,None,50,False,60,100,200,400]
total = 0
count = 0
for number in list:
    try:
        if not isinstance(number,bool) == True:
            total = total + number
            count = count + 1
            print(number)
    except TypeError:
        print("invalid value ",number, "therefore it is skipped")

print("total of whole list",total)
average = total / len(list)
print(f"Average = {average:.2f}",)
# task 
# findout total team score and lowest score and player