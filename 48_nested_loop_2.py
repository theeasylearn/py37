'''
1 0 1 0 1
1 0 1 0 
1 0 1
1 0
1
'''
line = 5
while line>=1: #outer loop
    letter = 1
    while letter<=line: #inner loop
        if letter%2==0:
            print('0',end=' ')
        else:
            print('1',end=' ')
        letter=letter+1
    print("")
    line=line-1

