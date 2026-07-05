# example of how to read data from file.
filename = "cars.txt"
mode = "r"

#read file
file = open(filename,mode)
print("file opened successfully")
print("_"*100)
print("File content")
print("_"*100)
count = 1
#display content
for line in file:
    print(line.strip()) #strip remove black line
    count=count+1
    if count%10==0:
        key = input("Press any key to continue")
print("Count of company = ",count-1)
#close file
file.close()

