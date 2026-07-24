import random as rd 
import string as st 
def generateRandomPassword(length=10):
    letters = st.ascii_letters + st.digits + "!@#$%^&*()-_=+"
    my_list = list(letters)
    rd.shuffle(my_list)
    return ''.join(my_list[0:length])


print(generateRandomPassword())
print(generateRandomPassword(20))