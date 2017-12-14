"""
Exercise 5.2
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 
"""
largest = None
smallest = None
nums = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    nums.append(num)
    nums.sort()    
for num in nums:
    try:
        if largest is None or int(num) > largest:
            largest = int(num)
        elif smallest is None and int(num) < largest:
            smallest = int(num)
        elif int(num) < largest and int(num) < smallest:
            smallest = int(num)
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)