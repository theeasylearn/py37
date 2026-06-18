#write a program to findout whether given number is prime number or not 
#input : 13 
#output : it is prime number 
#input : 9
#output : it is not prime number 

number = int(input('enter number to findout whether it is prime number or not'))
divisor = 2

while divisor<number:
    reminder = number % divisor
    if reminder == 0:
        print("it is not prime number")
        break # loop immediately stop 
    divisor = divisor + 1

if divisor==number:
    print('it is prime number')


