count = 0
largest_so_far = float("-inf")
while count < 5:
    num = int(input("give me a number:"))
    if num > largest_so_far:
        largest_so_far = num
        count += 1
        print("largest number is", largest_so_far)
6