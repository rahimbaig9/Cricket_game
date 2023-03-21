import random

def toss():
    print("Toss time! Heads (H) or tails (T)?")
    user_choice = input().upper()
    while user_choice not in ["H", "T"]:
        print("Invalid choice. Please choose H or T.")
        user_choice = input().upper()

    toss_result = random.choice(["H", "T"])
    if user_choice == toss_result:
        print("You won the toss!")
        return "user"
    else:
        print("You lost the toss.")
        return "system"

def choose_bat_or_bowl():
    print("What would you like to do? Bat (B) or bowl (W)?")
    user_choice = input().upper()
    while user_choice not in ["B", "W"]:
        print("Invalid choice. Please choose B or W.")
        user_choice = input().upper()
    return user_choice == "B"

def simulate_ball():
    runs = random.randint(0, 6)
    print("Runs scored:", runs)
    return runs

def bat(target, overs, players):
    score = 0
    overs_left = overs
    wickets = 0
    player_index = 0
    print("You are batting.")
    while overs_left > 0 and score < target and wickets < len(players) - 1:
        current_player = players[player_index]
        print(current_player + " is batting. " + str(wickets) + " wickets down.")
        print(overs_left, "overs left. Target:", target - score)
        input("Press enter to start the over.")
        runs_this_over = [simulate_ball() for i in range(6)]
        runs = sum(runs_this_over)
        print("Runs scored in this over:", runs)
        score += runs
        if runs == 0:
            wickets += 1
            print(current_player + " is out!")
        overs_left -= 1
        player_index += 1
        if player_index >= len(players):
            player_index = 0
    return score, wickets

def bowl(target, overs):
    score = 0
    overs_left = overs
    print("You are bowling.")
    while overs_left > 0 and score < target:
        print(overs_left, "overs left. Target:", target - score)
        input("Press enter to start the over.")
        runs_this_over = [simulate_ball() for i in range(6)]
        runs = sum(runs_this_over)
        print("Runs scored in this over:", runs)
        score += runs
        overs_left -= 1
    return score

def play_cricket():
    print("Welcome to the cricket game!")
    user_score = 0
    system_score = 0

    # Player names
    print("Enter the names of the players:")
    players = []
    for i in range(11):
        player_name = input("Player " + str(i+1) + ": ")
        players.append(player_name)

    # Toss
    winner = toss()

    # Batting and bowling
    if winner == "user":
        user_batting = choose_bat_or_bowl()
        if user_batting:
            print("You chose to bat.")
            target = random.randint(50, 150)
            user_score, wickets = bat(target, 20, players)
            system_score = bowl(user_score, 20)
        else:
            print("You chose to bowl")
            target = random.randint(80, 200)
            system_score = bowl(target, 20)
            user_score, wickets = bat(system_score + 1, 20, players)
    else:
        print("The system won the toss.")
        system_batting = choose_bat_or_bowl()
        if system_batting:
            print("The system chose to bat.")
            target = random.randint(50, 150)
            system_score, wickets = bat(target, 20, players)
            user_score = bowl(system_score, 20)
        else:
            print("The system chose to bowl.")
            target = random.randint(80, 200)
            user_score, wickets = bat(target, 20, players)
            system_score = bowl(user_score + 1, 20)

    # Display results
    print("You scored", user_score, "runs.")
    print("The system scored", system_score, "runs.")
    print("Wickets lost:", wickets)
    if user_score > system_score:
        print("Congratulations! You won the game.")
    elif user_score < system_score:
        print("Sorry, you lost the game.")
    else:
        print("The game is tied.")

# Start the game
play_cricket()

