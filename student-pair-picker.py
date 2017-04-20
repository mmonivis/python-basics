students = [
    "Marissa",
    "Merliee",
    "Daniel",
    "Chris",
    "Chad",
    "Shane",
    "Stephen",
    "Drew",
    "Guido",
    "Porscha",
    "Carla",
    "YingRong",
    "Ian",
    "Nick",
    "Michael",
    "Hayes"
]

# Take the list "students", randomly pair 2 until all students have been paired
import random

# for student in students(0,len(students))

def get_student():
    # Get a random number from the indicies left in students
    rand_num = random.randint(0,len(students)-1) # -1 so it includes the last person in the list
    current_student = students[rand_num]
    students.remove(current_student)
    return current_student

while students:
    student1 = get_student()
    student2 = get_student()
    print ("%s is paired with %s") % (student1, student2)

# while students:
#     get_student()
#     # Get a random number from the indicies left in students
#     rand_num = random.randint(0,len(students)-1)
#     # print (rand_num)
#     current_student = students[rand_num]
#     students.remove(current_student)
#     print current_student
#     rand_num = random.randint(0,len(students)-1)
#     current_student = students[rand_num]
#     students.remove(current_student)
#     print (" is paired with " + current_student)