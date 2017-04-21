# Print A Triangle

# Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******

# height = 4
# for i in range(1,height+1):
#     # print the padding (spaces)
#     spaces = (height-i) * 2 * " "
#     stars = ((i - 1) * 2 + 1) * "* "
#     print (spaces + stars)

# def print_star():
#     spaces = " " * (space_count / 2)
#     stars = "*" * star_count
#     print (spaces + stars + spaces)
# total_width = 10
# star_count = 1
# space_count = total_width - star_count
# loop_count = 1
# while loop_count <= 10:
#     if(star_count % 2 == 1):
#         print_star()
#     star_count += 1
#     space_count -= 1
#     loop_count += 1

# Print A Banner

# text = " Good morning, Vietnam "
# for i in text:
#     print(len(text) * "*") + "**"
#     print "*" + text + "*"
#     print(len(text) * "*") + "**"
#     break

# Print range of numbers
# for n in range(1,10+1):
#     print (n)

# Print with user prompts
# start = raw_input("Start from: ")
# end = raw_input("End on: ")
# for n in range(1,10):
#     print n

n=int(input("Enter the lenght of the rectangle: "))
m=int(input("Enter the width: "))
star="*"
def print_rect(n, m, star):
    for a in range(m):
        print (n*star)
print_rect(n, m, star)