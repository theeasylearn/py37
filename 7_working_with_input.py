# write a program to accept name, age, weight and gender
name = input("What is your name?")
age = input("What is your age?")
weight = input("What is your weight?")
gender = input("What is your gender?")

#display input 
print(name,age,weight,gender)

#add 10 into age variable
# must convert variable into integer/float before we do any mathematical operation
age = int(age)
weight = float(weight)

age = age + 10
print(age,weight)

#convert variables into number(integer/float)
