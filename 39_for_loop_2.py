#write a program to convert temperature in celsius into fahrenheit 
temperature = (41.5,40.9,35.6,33.2,30.11,27.25,21.20,18.70) #celsius
for temp in temperature:
    # print(temp)
    fahrenheit = (temp * (9/5)) + 32
    print(f"ceilsius = {temp} to fahrenheit = {fahrenheit:.2f}")