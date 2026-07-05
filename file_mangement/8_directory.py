import os 

#create directory 
os.mkdir("box")
key = input("Directory created, press any key to continue")

#change directory 
os.chdir('box')

#current working directory 
print(os.getcwd())


os.mkdir("small_box")
key = input("Directory created, press any key to continue")

os.rmdir('small_box')
print('directory has been removed')