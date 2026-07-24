import random as rd #rd is alias(nick name) for random 
colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Orange", "Purple", "Pink", "Brown"]
print("original list ",colors)
new_color = rd.sample(colors,k=5)
print("new color list ",new_color)
print("original list ",colors)

