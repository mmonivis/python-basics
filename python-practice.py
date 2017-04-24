x = 3

def calc():
    # x is now global
    global x
    x = x + 3
    # x = 5
    print x

calc()
print x