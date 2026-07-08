#default argument function 
def getTotalSeconds(hours,minutes=0,second=0):
    total_seconds = (hours * 3600) + (minutes * 60) + second
    return total_seconds


h  = int(input("Enter hours"))
m = int(input("Enter minutes"))
s = int(input("Enter seconds"))

print("function called with 3 arguments ",getTotalSeconds(h,m,s))
print("function called with 2 arguments ",getTotalSeconds(h,m))
print("function called with 1 arguments ",getTotalSeconds(h))
