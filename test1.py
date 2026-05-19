# Test 1: random practice
fruits = ["apple", "strawberry", "banana", "grape", "orange"]
fruits.append("watermelon")
print(fruits)

name = input("What is your name? ")
if len(name) > 3:
    name = name[:3]
age = input("What is your age? ")
user = name + "user" + age
print("Your username is: " + user)

rating = ""
print(user + ", rate the fruits from 1 to 5:")
for fruit in fruits:
    rate = input("" + fruit + ": ")
    rating = rating + fruit + " : " + str(rate) + ", "
    if fruit == "watermelon":
        rating = rating[:-2]
print("Your ratings are:",rating)