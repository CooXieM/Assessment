import random

low_num = 1
high_num = 10

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



for item in range(0,3):

    #Randomly generated number set between the chosen veriables.
    n1 = random.randint(low_num, high_num)
    n2 = random.randint(low_num, high_num)

    #Print the question
    print("{} * {} = ".format(n1, n2))

    ans = intcheck("Answer: ")
    if ans == (n1 * n2):
        print()
        print("*****You got it*****")
        print()

    else:
        print()
        print("?????Incorrect?????")
        print()