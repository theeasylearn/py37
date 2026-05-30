#example of dicitonary 
book = {'name':'learning python','author':'ankit patel','price':500,'pages':100,'weight':100.99}
print(book)

#update
book['name'] = 'Mastering Python'
#add new key value pair
book['publisher'] = 'T.E.L'

print(book)
del book['publisher']
print(book)
