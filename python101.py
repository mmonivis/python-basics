# print "Hello, World!"
# Print two different things on the same line
# print ("Hello, World", "Again")

# print """This
# will ignore
# the new lines
# until it sees
# another 3 double quotes"""

# Strings
first_name = "Marissa"
last_name = "Monivis"
print "Hello, {} {}".format(first_name, last_name)

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

import random
random_number = random.randint(1,10)

# Loop - Keep doing something until I tell you to stop
still_guessing = True;
while still_guessing:
    guess_a_number = raw_input("Guess a number between 1 and 10. ")
    if (int(guess_a_number) == random_number):
        print "You guessed the number!";
        still_guessing = False;


