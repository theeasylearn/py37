#print 1 to 10 in reverse order 
# 10 9 8 7 6 5 4 3 2 1 
def reverse_print(num): #9
    if num>=1:
        print(num,end=' ') # 9 
        num = num - 1 # 8
        reverse_print(num) #function called if self

num = 10
reverse_print(num)
