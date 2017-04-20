fullName = "Marissa Monivis"
age = 25

myArray = []
myArray.append(fullName)
myArray.append(age)
print myArray

def sayHello():
    print "Hello!"
sayHello()

split_name = fullName.split()
print (split_name)

def say_name():
    print("Hello, " + split_name[0] + "!")
say_name()

def my_age(birth_year):
    print(2017-birth_year)
my_age(1992)

def sum_odd_numbers():
    sum = 0
    for i in range (1,5001,2):
        sum += i
    return sum
print sum_odd_numbers()

# BREAK example
i = 0
while 1: # This will run forever...
        i += 1
        if (i == 1000):
            break
print ("We broke ouf of the loop!")