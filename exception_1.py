# example of exceptional handling mechanism 
# write a program to finder strike rate of batter using given runs and balls 
try:
    runs = int(input("Enter runs"))
    balls = int(input("Enter balls"))
    strike_rate = runs // balls
except ValueError:
    #this block will execute only if user do not give perfect input 
    print("runs and balls must be integer")
except ZeroDivisionError:
    #this block will execute only if balls are zero 
    print("balls can not be zero")
else:
    #this block will only execute if there is no error 
    print("Strike rate is ",strike_rate)
finally:
    print("thank you for using program")
