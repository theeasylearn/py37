#write a program to convert given minutes into hours and remaining minutes 
# input : 150 minutes output : 2 hours 30 minutes 
# input : 75 minutes output : 1 hours 15 minutes 

minutes = int(input("enter minutes"))

#convert into hours 
hours = minutes // 60 # + - * / % ** //
print("hours ",hours)
minutes = minutes % 60 # 30
print("minutes ",minutes)

