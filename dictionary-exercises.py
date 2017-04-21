# --------------- EXERCISE 1 ---------------- #

# Given:

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# Write code to do the following:

# Print Elizabeth's phone number.
print(phonebook_dict['Elizabeth'])

# Add an entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)

# Delete Alice's phone entry.
# phonebook_dict.pop('Alice')
del(phonebook_dict['Alice'])
print(phonebook_dict)

# Change Bob's phone number to '968-345-2345'.
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

# Print all the phone entries.
# print(phonebook_dict.values())
print(phonebook_dict)

# In this exercise, are you using dynamic keys or fixed keys?
# Fixed: Yellow = string, if font was white, it would be dynamic because it would be a variable


# --------------- EXERCISE 2 ---------------- #

# Given:

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Write a python expression that gets the email address of Ramit.
print ramit['email']

# Write a python expression that gets the first of Ramit's interests.
print ramit['interests'][0]

# Write a python expression that gets the email address of Jasmine.
print ramit['friends'][0]['email']

# Write a python expression that gets the second of Jan's two interests.
print ramit['friends'][1]['interests'][1]

# In this exercise, are you using dynamic keys or fixed keys?



# --------------- EXERCISE 3 ---------------- #

# Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}

# def letter_histogram(word):
#     empty_dict = {}
#     for n in word:
#         if n in empty_dict:
#             empty_dict[n] += 1
#         else:
#             empty_dict[n] = 1
#     print empty_dict

# user_word = raw_input("Type a word: ")
# letter_histogram(user_word)

# word_input = list(raw_input("Type a word: "))

# for i in word_input:
#     if i in empty_dict:
#         empty_dict[i] += 1
#     else:
#         empty_dict[i] = 1

# print empty_dict


# --------------- EXERCISE 4 ---------------- #

# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

# empty_dict_words = {}

# def para_histogram(word):
#     word_list = word.split()
#     for n in word_list:
#         if n in empty_dict_words:
#             empty_dict_words[n] += 1
#         else:
#             empty_dict_words[n] = 1
#     print empty_dict_words

# para_histogram("You are great. You are wonderful. You is cool.")


# --------------- EXERCISE 5 / BONUS ---------------- #

# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.



def letter_histogram(word):
    empty_dict_max = {}
    for n in word:
        if n in empty_dict_max:
            empty_dict_max[n] += 1
        else:
            empty_dict_max[n] = 1
    return empty_dict_max

# user_word = raw_input("Type a word: ")
# empty_dict_max = letter_histogram(user_word)
# chads_list = []
# for key in empty_dict_max:
#     chads_list.append([key,empty_dict_max[key]])
# chads_list.sort(key = lambda x: x[1])
# print chads_list[-1]
# print chads_list[-2]
# print chads_list[-3]

user_word = raw_input("Type a word: ")
empty_dict_max = letter_histogram(user_word)

max_key = ""
new_dict = {}
while len(new_dict.keys() <= 2):
    max_number = 0
    for i in empty_dict_max:
        if empty_dict_max[i] > max_number:
            max_number = empty_dict_max[i]
            max_key = i
    del empty_dict_max[max_key]
    new_dict[max_key] = max_number
print new_dict
