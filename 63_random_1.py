#generate random number 
import random as rd #rd is alias(nick name) for random 
print("random number between 0 and 1 ",rd.random())
print("float random number between 10 to 99",rd.uniform(10,99))
print("integer random number between 10 to 99",rd.randint(10,99))
print("integer random number between 10 to 100 divisible by 5",rd.randrange(10,100,5))

colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Orange", "Purple", "Pink", "Brown"]
print(colors)

print("any one randomly pick color",rd.choice(colors))
print("any two randomly pick color",rd.choices(colors,k=2))
