#write a program to convert 24 hours format user given time into 12 hours time. 
# input : 15 hours output 3 PM
# input : 11 hours output 11 AM
hours = int(input('Enter time in 24 hours format'))
#check hours are in valid range or not 
if hours<0 or hours>24:
    print("invalid hours")
else:
    if hours<12:
        print(hours," AM")
        
    if hours>12:
        hours = hours - 12 
        print(hours," PM")


