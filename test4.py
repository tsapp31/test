# Test 4: online exercises

# Q1: write a python function that accepts two integer numbers. If the product of
# the two numbers is less than or equal to 1000, return the product, otherwise 
# return the sum

num1 = int(input("Input the first integer: "))
num2 = int(input("Input the second integer: "))

if num1*num2 <= 1000:
    print("The product is",num1*num2)
else:
    print("The sum is",num1+num2)

# Q2: iterate through the first 10 numbers. In each iteration, print the current 
# number, the previous number, and their sum

for x in range(10):
    if x == 0:
        print("Current number:", x, "Previous number: None, Sum: None")
    else:
        print("Current number:", x, "Previous number:", x-1, "Sum:", x+(x-1))