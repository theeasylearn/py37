#write a program to count vowels in given string  (a,e,i,o,u)
word = input("Enter your name")
count = 0
vowels = ['A','E','I','O','U','a','e','i','o','u']
for letter in word:
    # print(letter)
    if letter in vowels:
        count= count + 1

print('no of vowels =',count)
