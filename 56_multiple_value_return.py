def getDetail(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    return minutes,hours,days 
seconds = int(input("Enter seconds"))

time = getDetail(seconds)
print(time)
