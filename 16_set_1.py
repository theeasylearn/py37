#example of set 
fruits = {'apple','mango','pineapple','banana','apple'}
#ignore duplicate value 
print(fruits)

#add new value
fruits.add('kiwi')
fruits.add('mango') #ignore

print(fruits)

fruits.remove('pineapple')
print(fruits)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#union 
union = set1.union(set2)

#intersection 
intersection = set1.intersection(set2)

difference = set1.difference(set2) #all value which is in set 1 but not in set 2

print("union",union)
print("intersection ",intersection)
print("difference ",difference)

