numbers = [-2, -1, 0, 1, 2, 3, 4]

# Print highest number in list
print max(numbers)

# Print lowest number in list
print min(numbers)

# Print even numbers
for x in numbers:
    if x % 2 == 0:
        print (x)

# Print positive numbers
for x in numbers:
    if x > 0:
        print (x)

# Print Positive Numbers II
for n in numbers:
    even = []
    if n % 2 == 0:
        even.append(n)
    print even

