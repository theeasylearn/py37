'''
        *
       * *
      * * *
     * * * *
    * * * * *
'''
for line in range(5,0,-1): #outer loop
    for space in range(1,line): #inner loop
        print(" ",end='')
    for letter in range(0,6-line): 
        print("* ",end='')
    print('')


