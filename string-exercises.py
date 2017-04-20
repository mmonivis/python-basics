# string = "hello, world!"
# print string.upper()

# Capitalize
# string_to_list = string.split()
# print string_to_list
# print string_to_list.capitalize()
# print string.capitalize()

# new_string = ""
# for i in string:
#     new_string += i.upper()
# print new_string

# Capitalize each word

# Reverse
# reverse_string = string[::-1]
# print (reverse_string)

#Leetspeak
# leetspeak = {
#     "A": "4",
#     "E": "3",
#     "G": "6",
#     "I": "1",
#     "O": "0",
#     "S": "5",
#     "T": "7"
# }

# string2 = "HELLO, TEAM!"
# for x, y in leetspeak.items():
#     string2 = string2.replace(x, y)
# print string2

# Long-Long Vowels

# def longword(string):
#     vowels = "aeiouAEIOU"
#     for vowel in vowels:
#         string = string.replace(vowel, vowel * 5, 2)
#     print string

# longword("Decent")

# CAESAR CIPHER

# key = 'abcdefghijklmnopqrstuvwxyz'

# def decrypt(n, ciphertext):
#     """Decrypt the string and return the plaintext"""
#     result = ''

#     for l in ciphertext:
#         try:
#             i = (key.index(l) - n) % 26
#             result += key[i]
#         except ValueError:
#             result += l

#     print result

# decrypt(13, "lbh zhfg hayrnea jung lbh unir yrnearq",)

# def decrypt_function(encrypted_letter):
#     if:
#     except:
#     else:
