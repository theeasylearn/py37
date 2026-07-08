stairs = int(input("Enter number of stairs: "))

if stairs == 0 or stairs == 1:
    print("Total ways = 1")
else:
    first = 1
    second = 1

    for i in range(2, stairs + 1):
        current = first + second
        first = second
        second = current

    print("Total ways =", second)