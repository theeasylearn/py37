#create arbitrary argument function
def getSum(*values):
    total = 0
    for item in values:
        total = total + item 
    return total


result = getSum(10,20,30,40)
print(result)
result = getSum(100,200,300,400,500,1000)
print(result)
result = getSum(100,200,300,400,500,1000,5000,8500)
print(result)
