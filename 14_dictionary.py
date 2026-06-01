match = {} 
print(match)

match['date'] = '30-06-2026'
match['venue'] = 'Ahmedabad'
match['time'] = '07:00 PM'
match['price'] = 1000

print(match)
#add teams into dictionary as tuple 
match['teams'] = ('Gujarat Titans','Royal Challenger Banglore')
#add players into match as list 
match['players'] = ['Virat Kohli','Rajat Patidar','Shubhnam Gill','Sai Surdershan','Bhuvi']
print(match)
#if key already exists, value of the key will be updated
match['venue'] = 'Mumbai'
del match['time'] #remove key value pair time
# del match['teams'][0]
# match['teams'][0] = ('Rajasthan Royals')
print(match)


