x:int = 0
while x <=100:
    print(x)

    x += 1
    if x%15==0:

        print("fizzbuzz")
    elif x%3==0:

        print("fizz")
    elif x%2==0:
        print("buzz")


