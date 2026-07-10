#example of keyword arguments 
def getMerit(maths,science,english,computer,history,drawing):
    print(f"maths={maths} ,science={science},english={english},computer={computer},history={history},drawing={drawing}")
    total = maths + science + english
    return total 

m = int(input("Enter Maths marks: "))
s = int(input("Enter Science marks: "))
e = int(input("Enter English marks: "))
c = int(input("Enter Computer marks: "))
d = int(input("Enter Drawing marks: "))
h = int(input("Enter History marks: "))
# print(getMerit(c,d,h,m,s,e))
print(getMerit(computer=c,drawing=d,history=h,maths=m,science=s,english=e))
