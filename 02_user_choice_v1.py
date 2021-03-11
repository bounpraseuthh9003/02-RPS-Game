# Functions goes here...
def choice_checker(question):

    valid = False
    while not valid:

        # Ask users for choice
        response = input(question).lower()

        if response == "rock" or response == "r":
                return response
        elif response == "paper" or response == "p":
                return response
        elif response == "scissors" or response == "s":
                return response
        else:
            print("Please pick r / p /s")

# Main routine goes here

# Ask user their choice of r / p / s - check if this is valid


# print out choice for comparison purposes
user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")
