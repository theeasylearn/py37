#example of logical expression 
a = int(input("Enter value for a"))
b = int(input("Enter value for b"))
c = int(input("Enter value for c"))


result = a < b and b < c
print(f"{result} = {a} < {b} and {b} < {c}")

result = a < b and b > c
print(f"{result} = {a} < {b} and {b} > {c}")

result = a > b and b > c
print(f"{result} = {a} > {b} and {b} > {c}")

result = a < b or b > c
print(f"{result} = {a} < {b} or {b} > {c}")

result = a > b or b > c
print(f"{result} = {a} > {b} or {b} > {c}")


result = not (a < b and b < c)
print(f"{result} = not {a} < {b} and {b} < {c}")

result = not (a > b or b > c)
print(f"{result} = not {a} > {b} or {b} > {c}")

