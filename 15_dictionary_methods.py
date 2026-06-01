#dictionary related methods 
product = {
    "id": 101,
    "name": "Laptop",
    "brand": "Dell",
    "category": "Electronics",
    "price": 55000,
    "quantity": 15,
    "color": "Black",
    "weight": "1.8 kg",
    "warranty": "1 Year",
    "rating": 4.5
}
print(product)
#copy dictionary into another variable
product_2 = product.copy()
print("Product 2 dictionary",product_2)
product_2.clear()
print("Product 2 dictionary",product_2)

#get only keys
print("only keys ", product.keys())
print("only values ", product.values())
print("both key and value ", product.items())

#remove key category
product.pop("category")

#remove last key value pair 
product.popitem()

print("now dictionary has ",product)
person_fields = ["surname", "name", "dob", "gender", "weight"]

#create dictionary using value of the list as key
kabir = dict.fromkeys(person_fields)
print(kabir)
kabir.update({'name':'kabir','surname':'patel','city':'bhavnagar'})
print(kabir)
print("value of surname key ",kabir.get('surname'))
print("value of mobile key ",kabir.get('mobile'))
print("value of mobile key ",kabir.get('mobile','not available'))