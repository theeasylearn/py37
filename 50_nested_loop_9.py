'''
    1
   12
  123
 1234
12345
'''
for line in range(5,0,-1): #outer loop
    for space in range(1,line): #inner loop
        print(" ",end='')
    for letter in range(1,7-line): 
        print(letter,end='')
    print('')


