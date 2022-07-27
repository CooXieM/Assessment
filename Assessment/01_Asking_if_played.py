#Ask user if they have played before
def statement_generator(statement, decoration):
    
    sides = decoration * 3

    statement = '{} {} {}'.format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


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

