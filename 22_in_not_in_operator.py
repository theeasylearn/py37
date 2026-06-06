#create list 
states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

vegetables = ("Potato", "Tomato", "Onion", "Carrot", "Cabbage", "Cauliflower", "Spinach", "Brinjal", "Peas", "Capsicum")

your_state = input("Where are you from (state)?")

isFound = your_state in states
print(isFound)

isNotFound = your_state not in states
print(isNotFound)

favorite = input("which is your favorite vegetable?")

isFound = favorite in vegetables
print(isFound)

fruits = "Apple Mango Banana Orange Grapes Pineapple Papaya Guava Watermelon Strawberry Kiwi Pomegranate Lychee Cherry Peach Pear Plum Coconut DragonFruit Muskmelon"

favorite = input("which is your favorite fruit?")
isFound = favorite in fruits
print(isFound)
