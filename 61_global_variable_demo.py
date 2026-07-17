balance = 2000

def AddMoney(amount):
    global balance
    balance = balance + amount 

amount = int(input("Enter amount"))
print("before update balance = ",balance)

AddMoney(amount)
print("after update balance = ",balance)
