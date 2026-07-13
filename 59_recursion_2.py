#write a program to convert given decimal number into binary number 
def binary(number): #62
    if number>0:
        reminder = number % 2 #1
        number = number // 2  # 62
        binary(number) #62
        print(reminder,end=' ')

number = 125
binary(number)

