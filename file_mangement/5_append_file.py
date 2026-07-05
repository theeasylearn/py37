# example of how to write data into file.

filename = input("Enter new file name")
mode = "a"

#read file
with open(filename,mode) as file:
    print("file opened successfully")
    print("_"*100)
    while True:
        content = input("type your friends name")
        file.write(content + "\n")
        if content == "":
            break #stop loop 
print("file created successfully ")
   

