#concept of string variable in python 
name = "the easylearn academy \n" #\n new line
city = " Bhavnagar "
address = " 105, eva surbhi, opp aksharwadi temple \n"
print(name)
detail = name + address + city #this will join 3 string into new string detail
print(detail)
print(city * 5)  #it will repeat city variable's value (bhavnagar) 5 times

#print line 
print("_"*100)

print(name[0:3]) #the 
print(name[4:13]) #easylearn
print(name[8:13]) #learn
print(name[14:21]) #academy
# or
print(name[14:])

#print 1st 3 letter
print(name[:3]) #the 