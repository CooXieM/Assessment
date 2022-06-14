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
user_input = ""
Question = 0
mode = "regular"

rounds = intcheck("Rounds:", 1, exit_code = "")
if rounds == "":
    print(" you chose infinite mode")
    mode = "infinite"
    rounds = 10

# rounds loop starts here
end_game = "no"
while Question < rounds and end_game == "no":

    if mode == "infinite":
        rounds += 1
        heading = "----- Round {} -----".format(Question + 1)
    else:
        heading = "----- Round {} of {} ------".format(Question + 1, rounds)
    
    if user_input == "xxx":
        break
    print()
    print(heading)