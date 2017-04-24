# print "Hello, World!"
# Print two different things on the same line
# print ("Hello, World", "Again")

# print """This
# will ignore
# the new lines
# until it sees
# another 3 double quotes"""

# Strings
# first_name = "Marissa"
# last_name = "Monivis"
# print "Hello, {} {}".format(first_name, last_name)

# print "Hello, %s %s" % (first_name, last_name)
# print "Hello, %s %s for the %drd time." % (first_name, last_name, 3)

# Floats

# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)

# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer

# Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

# Conditionals
# 1 = means you want to assign something left with right
# 2 == means you want to compare left with right

# if(first_name == last_name):
#     print "Your first name is the same as your last name?"

# age = raw_input("How old are you?")
# age_as_int = int(age)
# # print type(age)
# if (age_as_int >= 21):
#     print "You can buy beer."
# else:
#     print "You are underage."

# import random
# random_number = random.randint(1,10)

# # Loop - Keep doing something until I tell you to stop
# still_guessing = True;
# while still_guessing:
#     guess_a_number = raw_input("Guess a number between 1 and 10. ")
#     if (int(guess_a_number) == random_number):
#         print "You guessed the number!";
#         still_guessing = False;

# --------------- DAY 3 --------------- #

# students = [
#     "Marissa",
#     "Merilee",
#     "Daniel",
#     "Chris",
#     "Chad",
#     "Shane",
#     "Stephen",
#     "Drew"
# ]

# The first element in a list is always 0, the second element is always 1

# print(students[0])
# print(students[-1])

# atlantaTeams = [
#     "Falcons",
#     "Braves",
#     "Hawks",
#     "Thrashers"
# ]

# print (atlantaTeams[0])

# To add an element to the END of a list, you can use the append method
# atlantaTeams.append("Atl United")
# print (atlantaTeams)

# Pop -- REMOVES the last item on the list
# students.pop()
# print students

# To delete an index, you can use the remove method
# atlantaTeams.remove("Thrashers")
# print (atlantaTeams)

# We can insert into any indicie with the insert method
# atlantaTeams.insert(0, "Tom Brady's Team")
# print (atlantaTeams)

# teams_as_a_string = "Falcons, Braves, Hawks, Thrashers"
# teams_as_a_list = teams_as_a_string.split(",")
# print (teams_as_a_list)

# Sort will CHANGE the list
# atlantaTeams.sort();
# print (atlantaTeams)

# Sorted will sort, but NOT change the list
# copy_of_atlanta_teams = sorted(atlantaTeams);
# print (copy_of_atlanta_teams)

# Reverse
# copy_of_atlanta_teams.reverse();
# print (copy_of_atlanta_teams)

# length_of_atlanta_teams = len(copy_of_atlanta_teams)
# print (length_of_atlanta_teams)

# print len(copy_of_atlanta_teams[0])

# The other type of loop... For
# for i in range(1,10):
#     print i

# For Loop Format:
# [for] [what_you_want_to_call_the_thing_you_are_on] [in] [variable_looping_through]
# for student in students:
    # print student

# Set up for a loop... but the range, will be 0 to len-1
# students_length = len(students)
# for i in range(0,students_length):
#     print (students[i])

# List in increments of 2
# for i in range(0,10,2):
#     print (i)

# If you want a portion of a list, you can use the [x:y] format
# print(students)
# second_and_third = students[1:3]
# print second_and_third
# print (students)
# all_but_the_first = students[1:] # same as all_but_the_first = students[1:len(students)]
# print all_but_the_first

# --

# FUNCTIONS
# To declare a function, use "def" -- Functions ALWAYS have ()
# def say_hello():
#     print ("Hello")

# # say_hello()

# def say_hello_with_name(name): # "name" is a local variable, can ONLY be used within this function
#     print ("Hello, " + name)

# # say_hello_with_name() #this will fail!
# # say_hello_with_name("Rob", "Chad") #this will fail!
# # say_hello_with_name("Rissa")

# def say_hello_with_default(name, in_class = "Yes"):
#     print ("Hello, " + name)
#     print "Is student in class? " + in_class

# say_hello_with_default("Rob",)
# say_hello_with_default("Mary", "No")

# # Functions always return something
# def return_user_name(name):
#     return name

# print return_user_name("Rissa")

# def make_uppercase(string):
#     return string.upper()

# normalized_string = make_uppercase("iM a WiLd ANd CraZY GuY")
# print normalized_string



# --------- DAY 4 ----------- #



# TUPLE = Same as list... EXCEPT:
# 1. Values cannot be changed
# 2. It uses () instead of []

# a_tuple_test = (1,5,8)
# print a_tuple_test[1]
# Test the tuple
# a_tuple_test[1] = 6 # Will pull up error

# DICTIONARIES
#    Very simple objects; operate with a "key-value pair" (associates data TOGETHER)
# name = "Rissa"
# gender = "Female"
# height = "5'2"

# person = {
#     "name": "Rissa",
#     "gender": "Female",
#     "height": "5'2"
# }

# print(person["name"])
# print(person["gender"])
# print(person["height"])

# zombie = {}
# zombie['weapon'] = "axe"
# zombie['health'] = 100
# zombie['startX'] = 10
# zombie['startY'] = 20

# print zombie

# for key, value in zombie.items():
#     print "Zombie has a key of %s with a value of %s" % (key, value)
#     print (zombie[key])

# if (zombie["speed"] <= 5):
#     zombie["position"] = zombie[startX] + 5
# elif (zombie["speed"] <= 10):
#     zombie["position"] = zombie[startX] + 10
# else:
#     zombie["position"] = zombie[startX] + 15

# zombie['pointless'] = "Why?"
# print zombie
# # remove key + value
# del zombie['pointless']
# print zombie

# player_push = "up"
# # variable key names
# if (player_push == "up"):
#     direction = "startY"
# else:
#     direction = "startX"
# zombie[direction] += 10

# zombies = []
# zombies.append({
#     'speed': 10,
#     'weapon': 'fist',
#     'name': 'Hank'
# })
# zombies.append({
#     'speed': 5,
#     'weapon': 'baseball bat',
#     'name': 'Bruiser'
# })

# # get the second zombie's speed...
# print (zombies[1]['speed'])

# zombies[1]['victims'] = [
#     'Jane',
#     'Mike',
#     'Bob'
# ]

# print (zombies[1]['victims'][2])


# ---

x = 3
y = 0

def get_number():
    global y
    y = 5
    a = 2

def calc():
    # x is now global
    global x
    x = x + y
    # x = 5
    print x

print y
get_number() # this will change global y from 0 to 5
calc()
print x