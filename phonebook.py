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

def set_an_entry(name, phone_number):
    new_dict = {"name": name, "phone_number": phone_number}
    phonebook_data.append(new_dict)
    os.system("clear")
    print ("%s has been added.\n" % name)

def Delete_an_entry(name):
    for n in phonebook_data:
        if name in n.values():
            phonebook_data.remove(n)

def list_all_entry(phone_book):
    print (phone_book)

def search_entry(data):
    for n in phonebook_data:
        if data in n.values():
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
            user_name = raw_input("> ")
            print ("Please enter a phone number:\n")
            user_number = raw_input("> ")

            set_an_entry(user_name, user_number)

        # DELETE AN ENTRY
        elif (convert_user == 3):
                del_user = raw_input("Who would you like to remove?\n ")
                Delete_an_entry(del_user)
                print ("Entry has been removed.\n")

        # LIST ALL ENTRIES
        elif (convert_user == 4):
                list_all_entry(phonebook_data)

        # SEARCH FOR AN ENTRY
        elif (convert_user == 5):
                data_user = raw_input("Enter a name or phone number:\n")
                print(look_up_entry(data_user))

        # QUIT
        elif(convert_user == 6):
            # User chose to quit, so leave the loop
            print ("Exit.")
            break



