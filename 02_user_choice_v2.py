# Version 2 - checks that response is in a given list / is valid


# Functions goes here...
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask users for choice - make sure choice is lowercase
        response = input(question).lower()

        # Goes through list, if response is an item in the list
        # (or the first letter of an item), the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

                # Output error if item not in list
            print(error)


# Main routine goes here


# Lists of valid responses
rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check if it is valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", rps_list,
                                 "Please choose from rock / paper / scissors (or xxx to quit) ")
