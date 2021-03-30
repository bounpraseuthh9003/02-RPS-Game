played_before = ""
instructions = "**** How To Play ****\n" \
               "\n" \
               "- Choose the amount of rounds you want to play \n" \
               "or press <enter> for infinite mode\n" \
               "\n" \
               "For each round, choose from rock / paper / scissors (or xxx to quit)\n" \
               "You can type r / p / s / x if you do not want to type the entire word.\n" \
               "\n" \
               "The rules are...\n" \
               "- Rock beats scissors\n" \
               "- Scissors beats paper\n" \
               "- Paper beats rock\n" \
               "\n" \
               "*** Have Fun Playing ***\n" \
               "\n" \
               "Program continues "

while played_before.lower != "xxx":
    # Ask the user if they have played before
    played_before = input("Have you played this game before? ").lower()

    # If they say yes, program continues
    # If they say no, show instructions
    # If it is an invalid answer, "please enter y/n"
    if played_before == "yes" or played_before == "y":
        played_before = "yes"
        print("Program continues")
        break

    elif played_before == "no" or played_before == "n":
        played_before = "no"
        print()
        print(instructions)
        break

    else:
        print("Please type yes / no")
        print()
