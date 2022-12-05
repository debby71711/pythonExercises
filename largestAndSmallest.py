number = int(input("Enter a number and enter 0 to end"))
smallest = largest = number

number =1
while number != 0:
    number = int(input("Enter another number"))

    if number > largest:
        largest = number
    if number <= smallest:
        smallest = number
        print(" largest is", largest)
        print("smallest is", smallest)
