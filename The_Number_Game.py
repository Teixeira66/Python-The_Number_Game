#setup
import random
answer = random.randint(1, 101)
user_winner = False
attempts = 0
attempt_word = ""

#Game Loop( the body of the loop inside)

while user_winner != True:

    #User input

    guess = input("Can you guess a number between 1 and 100? ")

    #Check The user Input
    try:
        guess_number = int(guess)
    except:
        print("You should write a number!")
        quit()

    #Increase attempt count
    attempts += 1

    #check the user answer against the secret number
    if guess_number == answer:
        user_winner = True
    elif guess_number > answer:
        print("The number is Smaller!!")
    else:
        print("The number is Bigger!!")

    #Get the spelling of the "attempt" word
    if attempts == 1:
        attempt_word = " attempt"
    else:
        attempt_word = " attempts"

    #Display the result
    if guess_number == answer:
        print("Congratulations!! You did it in " + str(attempts) + attempt_word)