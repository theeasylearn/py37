# different type of user defined function 
import shutil
#without return value without argument function 
def PrintLine():
    size = shutil.get_terminal_size()
    column = size.columns
    print("_"*column)

# without return value with argument function 
def PrintMessage(msg):
    size = shutil.get_terminal_size()
    column = size.columns
    print(msg.center(column))
# with return value without argument function 
def GetPi():
    #local variable 
    pi = 22/7
    return pi 
PrintLine()
msg = "THE EASYLEARN ACADEMY"
PrintMessage(msg)
PrintLine()
pi = GetPi()
print(pi)
