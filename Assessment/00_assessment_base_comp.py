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
    Welcome to the basic facts true or false game, to play you will be asked a question, you must answer
    with true or false. At the end of the game your results will be displayed. You are also allowed to pick how
    many rounds you want""")
    print()
    return ''
print()
statement_generator("Welcome to the basic facts game", "*")
print()

played_before = yes_no('have you played the game before? ')

if played_before =='no':
    instructions()
else:
    print("Program Continues")

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

rounds_played = 0
mode = "regular"

rounds = intcheck("Rounds:", 1, exit_code = "")
if rounds == "":
    mode = "infinite"
    rounds = 10

# rounds loop starts here
end_game = "no"
while rounds_played < rounds and end_game == "no":

    if mode == "infinite":
        rounds += 1
        heading = "----- Round {} -----".format(rounds_played + 1)
    else:
        heading = "----- Round {} of {} ------".format(rounds_played + 1, rounds)