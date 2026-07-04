# write a program to generate simpleInterest of given amount, rate, year using user defined function 
#create user defined function 
def GetSimpleInterest(amount,rate,year):
    #local variable
    res = (amount * rate * year) / 100
    return res   



a = int(input("Enter amount"))
r = float(input("Enter rate"))
y = int(input("Enter year"))
#function call 
result = GetSimpleInterest(a,r,y)
print("Interest ",result)