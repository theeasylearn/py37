# example of how to read data from file.
filename = "cars.txt"
mode = "r"

#read file
with open(filename,mode) as file:
    print("file opened successfully")
    print("_"*100)
    print("File content")
    print("_"*100)
    #display content
    content = file.read() #read method extract(read) all line from files 
    print(content)
   

