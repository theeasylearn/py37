#write a program to count vowels in given string  (a,e,i,o,u)
word = input("Enter your name")
count = 0
for letter in word:
    # print(letter)
    if letter == 'a' or letter=='e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter=='E' or letter == 'I' or letter == 'O' or letter == 'U':
        count= count + 1

print('no of vowels =',count)
