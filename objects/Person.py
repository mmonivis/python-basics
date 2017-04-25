class Person(object): # Need to pass object in Python 2
    def __init__(self,name,gender,cell):
        self.name = name
        self.gender = gender
        self.species = "Human" # Every object that gets created is going to have this.
        # self.number_of_arms = number_of_arms
        self.phone = {
            "cell": cell,
            "home": "Who has a home phone anymore?"
        }
        # pointless_variable = "Congress" -- Won't print to the object because it's not attached to self
        # print pointless_variable (unless this is included in the class)

    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person, self.name)

    def print_contact_info(self):
        if(self.phone['cell'] != ""):
            print "%s's number is %s" % (self.name, self.phone['cell'])

marissa = Person("Marissa", "female", "770-777-7777")
print marissa.name + " " + marissa.gender
print marissa.species
merilee = Person("Merilee", "female", "404-777-7777")
print merilee.species
merilee.species = "Robot"
print merilee.species
# print merilee.number_of_arms
print marissa.phone['cell']
print marissa.phone['home']

marissa.greet("Rob")
marissa.print_contact_info()
merilee.print_contact_info()

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print self.year, self.make, self.model

    def change_year(self, new_year):
        self.year = new_year

    def get_year(self):
        return self.year

marissas_car = Vehicle("Lexus", "RCF", "2015")
marissas_car.print_info()
marissas_car.change_year(2016)
# marissas_car.year = 2016 -- Shouldn't use this method, especially when it comes to large coding documents.
print marissas_car.get_year()
