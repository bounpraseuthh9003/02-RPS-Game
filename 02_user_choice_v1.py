# Functions goes here...
def choice_checker(question):

    valid = False
    while not valid:

        # Ask users for choice
        response = input(question)

        if response == "rock" or response == "r":
                return response

# Main routine goes here

# Ask user their choice of r / p / s - check if this is valid


# print out choice for comparison purposes
user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")
