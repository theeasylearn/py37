# write a program to convert given 2 digit amount into words 
# input : 84 output eight four
# input : 19 output one nine 

words = ['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine '] 
amount = int(input("Enter 2 digit amount"))
first = amount // 10 # 8
last = amount % 10  #4 
# print(last,first)
print(words[first],words[last]) 