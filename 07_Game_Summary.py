summary = []

rounds_lost = 0
rounds_draw = 0
rounds_played = 5

for item in range(0, 5):
    result = input("Choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "tie":
        rounds_draw += 1

    summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_draw

# calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_draw / rounds_played * 100

print()
print("***** Game History *****")
for game in summary:
    print(game)

print()

# display game stats & values to nearest whole number
print("******** Game Statistics ********")
print("Win: {}, ({:.0f}%)\nLost: {}, ({:.0f}%)\nDraw: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,
                                                                         percent_lose, rounds_draw, percent_tie))
