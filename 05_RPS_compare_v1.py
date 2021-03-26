# RPS Component 3 - Compare user choice and computer choice


rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    if __name__ == '__main__':
        for item in rps_list:
            user_choice = rps_list[user_index]
            comp_choice = rps_list[comp_index]
            user_index += 1

            # Compare option..
            user_choice = input("Please pick rock / paper / scissors ").lower()

            if user_choice == "rock" or user_choice == "r":
                user_choice = "rock"
                print("rock")

            elif user_choice == "paper" or user_choice == "p":
                user_choice = "paper"
                print("paper")

            else:
                user_choice = "scissors"
                print("scissors")

        print(" You chose {}, the computer choice {}. Results: {}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()
