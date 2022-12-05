number = int(input("enter a number: "))
factor = 1
sum_of_factor = 0

while factor < number:

    if number % factor == 0:
        sum_of_factor += factor

    factor += 1

if sum_of_factor > number:
    print("is deficient")
elif sum_of_factor > number:
    print("abundant")
else:
    print("perfect number")
