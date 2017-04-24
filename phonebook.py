# import stuff
import os

# Main Loop

phonebook_data = [
    {
        "name": "Melissa",
        "number": "404-235-5428"
    },
    {
        "name": "Joe",
        "number": "404-235-2125"
    },
    {
        "name": "Mike",
        "number": "770-134-2229"
    },
    {
        "name": "Igor",
        "number": "770-233-3461"
    }
]

def look_up_entry(name):
    for n in phonebook_data:
        if name in n.values():
            os.system("clear")
            return n
        else:
            os.system("clear")
            print ("%s is not in the list. Try again!\n") % (name)

while 1:
    print """Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Search for an entry
6. Quit
    """

    # CHOOSE WHAT YOU WANT TO DO:
    user_input = raw_input("What do you want to do (1-6)? ")
    # raw_input comes in as what data type? -- string! We are expecting an int...
    # Option 1: if(user_input == "1")
    # Option 2:
    try:
        convert_user = int(user_input)
    except ValueError:
        os.system("clear")
        print "You must enter a number!\n"
    else:
        # LOOK UP ENTRY
        if (convert_user == 1):
            name_user = raw_input("Who do you want to look up?\n")
            print (look_up_entry(name_user))
        # SET AN ENTRY
        elif (convert_user == 2):
            print ("Please enter a name:\n")
            user_name = input("> ")
            print ("Please enter a phone number:\n")
            user_number = input("> ")
        # DELETE AN ENTRY
        # LIST ALL ENTRIES
        # SEARCH FOR AN ENTRY
        # QUIT
        elif(convert_user == 6):
            # User chose to quit, so leave the loop
            break



