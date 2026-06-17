#write a program to print below sequence (only one number at time)
# 1 4 9 16 25 .... 1000
# 1 2 3 4  5 ..... 

num  = 1
while num<32:
    square = num * num 
    print(square,end=' ')
    num  = num + 1

