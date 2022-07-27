# Functions used to check input is valid
def check_rounds():
    while True:
        response = input("How many rounds (Press <Enter> For Infinite Mode): ")

        round_error = "please type either <enter> (For infinite mode) or an interger that is more than 0"
        if response != "":
            try:
                response = int(response)
                if response <1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response

# main routine goes here
rounds_played = 0
# ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

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

    rounds_played +=1
print("thank you for playing")