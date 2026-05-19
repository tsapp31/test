# Test 2: function practice
car = {
    "make":input("Car make: "),
    "model":input("Car model: "),
    "plate":input("Liscence plate: "),
    "year":input("Year: ")
}

def car_info(car):
    print("You drive a " + car["year"] + " " + car["make"] + " " + car["model"] + " with the liscence plate " + car["plate"].upper())

car_info(car)