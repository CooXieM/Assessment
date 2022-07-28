from random import randint
import math
import random
from re import X

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
print()
statement_generator("Welcome to the Multiplication Quiz", "*")
print()

#ask user if they have played before if not, print instructions
played_before = yes_no('have you played the game before? ')

#print instructions
def instructions() :
    print()
    print('**** How To Play ****')
    print("""
    Welcome to the Basic Facts game, to play you will be asked a low and high number and you will be told
    how many guesses you are allowed. Then you are to state how many Questions you want or press <Enter> for infinite
    mode. The game is simple, you will be asked a question reguarding Multiplication.
    At the end of the game you will have your score shown... Goodluck player.""")
    print()
    return ''
if played_before =='no':
    instructions()

# Functions used to check input is valid        
def intcheck(question, low=None, high=None, exit_code = "xxx"):

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

# game history
game_history = []
total_ans = []
ans = 0
#Users lowest and highest numbers
low_num = intcheck("Enter the lowest number ", low=0)
high_num = intcheck("Enter the highest number ", low=low_num)

range = high_num - low_num + 1
max_raw = math.log2(range)  #finds maximum # of guesses using
max_upped = math.ceil(max_raw)  #rounds up ( ceil -> ceiling)

#infinite mode
rounds = intcheck("How many Questions?:", 1, exit_code = "")
if rounds == "":
    mode = "infinite"
    rounds = 1

# rounds loop starts here
end_game = "no"
while rounds_played < rounds and end_game == "no":

    #If infinite mode make sure it doesn't end
    if mode == "infinite":
        rounds += 1

    num_guesses = 0
    #Starting infinite mode
    if mode == "infinite":
        heading = "----- Question {} -----".format(rounds_played + 1)
    else: #start normal mode
        heading = "----- Question {} of {} ------".format(rounds_played + 1, rounds)
    
    rounds_played += 1
    #printing heading
    print()
    print(heading)

    #Randomly generated number set between the chosen veriables.
    n1 = random.randint(low_num, high_num)
    n2 = random.randint(low_num, high_num)

    #Print the question
    print("{} X {} = ".format(n1, n2))
    
    #Adding the feedback of how many questions answered for both infinite and normal modes. :)
    if mode == "infinite":
        feedback = "Questions Answered = {}".format(rounds -1)
    else:
        feedback = "Questions Answered = {}".format(rounds)


    #answering the question and replying with if you got the right answer or not.
    ans = intcheck("Answer: ")
    if ans == (n1 * n2):
        print()
        print("*****You got it*****")
        rounds_won =+ 1
    else:
        print()
        print("?????Incorrect?????")
        print()
    
    if ans == (n1 * n2):
        ans += 1
    
    if ans == "xxx":
        break

    
print("---------------------")
print()
print("***Here are your results***")

# make rounds lost work using rounds played and rounds won
rounds_lost = rounds_played-rounds_won

# print basic, overall stats
print()
print("Questions Answered: {}".format(rounds_played))
print("Questions Lost: {} ".format(rounds_won))
print("Questions Won: {}".format(rounds_lost))


#thank user for playing
print()
print("Thank You For Playing")
print()
