# import random
# secret_number = random.randint(1,10);
# print secret_number

secret_number = 5
attempts = 5
still_guessing = True;

while (attempts > 0):
    print "You have"
    guess_a_number = raw_input("I am thinking of a number between 1 and 10... ")
    if (int(guess_a_number) == secret_number):
        print "Yes! You're right!";
        still_guessing = False;
    elif int(guess_a_number) > secret_number:
        print "%d is too high. You have %d tries left." % (int(guess_a_number), attempts)
    elif int(guess_a_number) < secret_number:
        print "%d is too low. You have %d tries left." % (int(guess_a_number), attempts)
    attempts -= 1
    if attempts == 0:
        print "You ran out of guesses!"
        still_guessing = False
        play_again = raw_input("Would you like to play again? (Y or N) ")

        if play_again == "Y":
            still_guessing = True
            attempts = 5
        if play_again == "N":
            print "Bye!"