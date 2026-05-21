# Test 6: python classes
class myclass:
    age = 21
    name = "Taylor"
    major = "ASE"
    dob = "06-18-2004"


class personal_info:
    species = "Human"
    def __init__(self,name, age, major, dob):
        self.name = name
        self.age = age
        self.major = major
        self.dob = dob


taylor = personal_info("Taylor", 21, "ASE", "06-18-2004")
print(taylor.name)
cody = personal_info("Cody",20,"ASE","04-18-2006")
print(cody.major)
print(cody.species)