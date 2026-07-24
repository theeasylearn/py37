#write a program to generate 6 digit otp 
import random as rd 
def getOTP():
    pair1 = rd.randint(10,99) #85
    pair2 = rd.randint(10,99) #80
    pair3 = rd.randint(10,99) #69
    otp = str(pair1) + str(pair2) + str(pair3)
    return otp 

print("6 digit otp ",getOTP()) 
print("6 digit otp ",getOTP()) 
print("6 digit otp ",getOTP()) 
