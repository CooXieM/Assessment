import math
#ask if the user has played the game before and print instructions.
def statement_generator(statement, decoration):
    
    sides = decoration * 3

    statement = '{} {} {}'.format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""
#the users Yes or No answer to if they have played before
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return "yes"

        elif response == 'no' or response == 'n':
            return "no"
        else:
            print ('please answer yes / no') 

#print instructions
def instructions() :
    print()
    print('**** How To Play ****')
    print("""
    Welcome to the Basic Facts game, to play you will be asked a low and high number and you will be told
    how many guesses you are allowed. Then you are to state how many rounds you want or press <Enter> for infinite
    mode. The game is simple, you will be asked a question reguarding Addition, Multiplication, Subtraction and Division.
    At the end of the game you will have your score shown... Goodluck player.""")
    print()
    return ''
print()
statement_generator("Welcome to the basic facts game", "*")
print()

played_before = yes_no('have you played the game before? ')

if played_before =='no':
    instructions()

# Functions used to check input is valid        
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

#rounds generator
rounds_played = 0
mode = "regular"

guess_history = []
game_history = []

low = intcheck("Low Number: ")
high = intcheck("High Number :", low + 1)

range = high - low + 1
max_raw = math.log2(range)  #finds maximum # of guesses using
max_upped = math.ceil(max_raw)  #rounds up ( ceil -> ceiling)
max_guesses = max_upped + 1

print("Max Guesses: {}".format(max_guesses))

#infinite mode
rounds = intcheck("Rounds:", 1, exit_code = "")
if rounds == "":
    mode = "infinite"
    rounds = 10

end_game = "no"
while rounds_played < rounds and end_game == "no":
    #start of game play loop
    #rounds heading
    print()
    if rounds == "":
        heading = "continuous Mode: Round {}".format(rounds_played + 1)
        
    else:
        heading = "round {} of {}".format(rounds_played + 1, rounds)
        
    print(heading)
    choose = input("Type xxx to end or press Enter to continue: ")

    #end game if exit code is typed
    if choose == "xxx":
        break

    # ***** rest of loop / game *****
    print("Your Answer {}".format(choose))

    

print()
print("Thank You For Playing")
print()