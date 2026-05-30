#create list 
fruits = ["apple", "banana", "mango", "orange", "grapes"]
vegetables = ["potato", "tomato", "onion", "carrot", "cabbage"]

print(fruits,vegetables)

#append new item into list at the end 
fruits.append('kiwi')

#insert new item just before banner (banana is at 1st position)
fruits.insert(1,'cherry')

#insert new item at beginning 
fruits.insert(0,'coconut')

print("after insertion fruits has",fruits)

# merge two list 
fruits.extend(vegetables)
print("extended fruits ",fruits)
#remove items from list (by value)
vegetables.remove('onion')

#remove item from list (by position(index))
vegetables.pop(3)

print("after deletion vegetables has ",vegetables)
print("position of tomato ",vegetables.index('tomato'))
# print("position of onion ",vegetables.index('onion')) #value error 

vegetables.clear()
print("now vegetables has",vegetables)

#delete list 
del vegetables
# print(vegetables)

#sort list fruits
fruits.sort()
print("sorted fruits ",fruits)
#reverse the list
fruits.reverse()
print("reversed fruits ",fruits)
print("count of apples ",fruits.count('apple'))

# fruits_2 = fruits #create reference means alias of fruits does not actually copy fruits 
# then how to copy list into another list 
fruits_2 = fruits.copy()
fruits.clear()
print(fruits,fruits_2)