#write a program to print below sequence (only one number at time)
# 0 1 1 2 3 5 8 13 21 .... 1000
#     l c n
# l = last 
# c = current
# n = next 
last = 0
current = 1
next = 1
print(last,end=' ') 
print(current,end=' ') 

while next<987: 
    next = last + current 
    print(next,end=' ')
    last = current 
    current = next 

