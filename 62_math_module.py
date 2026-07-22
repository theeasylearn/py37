import math
amount = float(input("Enter amount")) #3.25

floor_value = math.floor(amount) #3 
print("floor value",floor_value)
ceil_value = math.ceil(amount) #4
print("ceil value",ceil_value)
truncated_value = math.trunc(amount) 
print("truncated value",truncated_value)
different_value = math.modf(amount)
print("different value",different_value)
new_value = math.copysign(amount,-1) 
print("new value",new_value)
absolute_value = math.fabs(new_value) 
print("absolute value",absolute_value)
factorial_value = math.factorial(int(absolute_value))
print("factorial value",factorial_value)
reminder = math.fmod(10,3)
print("reminder value",floor_value)
