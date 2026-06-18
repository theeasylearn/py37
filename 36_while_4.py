#write a program to findout sum of all digits in given number 
#input : 12345 process : 1+2+3+4+5 output 15
amount = int(input("Enter amount"))
sum = 0 

while amount>0:
    reminder = amount%10 #5
    sum = sum + reminder
    amount = amount // 10
print(sum)
