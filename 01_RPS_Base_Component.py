import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")
        round_error = "Please type either <enter> or an integer that is more than 0 "

        # If Infinite Play Mode not chosen, check response
        # Make sure it is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of the loop
                if response < 1:
                    print(round_error)
                    continue

            # If response not an integer, go back to
            # start of the loop
            except ValueError:
                print(round_error)
                continue

        return response


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
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask users if they have played before
# if 'yes', show instructions

# Ask users for # of rounds then loop...

rounds_played = 0

# Ask users for # of rounds then loop, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Infinite Play Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instructions = "Please choose rock (r), paper (p) or scissors (s) or 'xxx' to exit: "
    choose_error = "Please choose from rock / paper / scissors (or xxx to quit)"

    # Ask user for choice and check if it is valid
    choose = choice_checker(choose_instructions, rps_list, choose_error)

    # Get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # Compare Choices

    # End game if exit code is typed
    if choose == "xxx":
        break

    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history
# if 'yes' show game history

# Show game statistics
