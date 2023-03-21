import random

def toss(player1, player2):
    """Function to simulate a toss"""
    toss_winner = random.choice([player1, player2])
    print(toss_winner, "won the toss!")
    choice = input("What do you choose? 'bat' or 'bowl'? ")
    if choice.lower() == "bat":
        bat_first = toss_winner
        bowl_first = player2 if toss_winner == player1 else player1
    else:
        bat_first = player2 if toss_winner == player1 else player1
        bowl_first = toss_winner
    return bat_first, bowl_first

def play_ball(player_name):
    """Function to simulate a ball"""
    run = random.choice([0, 1, 2, 3, 4, 5, 6, "out"])
    if run == "out":
        print(player_name, "is out!")
    else:
        print(player_name, "scores", run, "runs.")
    return run

def bat(target, overs, players):
    """Function to simulate batting"""
    wickets = 0
    runs = 0
    overs_played = 0
    player_index = 0
    while overs_played < overs and wickets < 10:
        player_name = players[player_index % len(players)]
        ball_score = play_ball(player_name)
        if ball_score == "out":
            wickets += 1
            if wickets < 10:
                print("Score:", runs, "-", wickets, "after", overs_played, "overs")
                print("Next batsman:", players[(player_index+1) % len(players)])
        else:
            runs += ball_score
        overs_played = int(player_index / len(players))
        player_index += 1
    print("Score:", runs, "-", wickets, "after", overs_played, "overs")
    return runs, wickets

def bowl(target, overs, players):
    """Function to simulate bowling"""
    wickets = 0
    runs = 0
    overs_played = 0
    player_index = 0
    while overs_played < overs and wickets < 10:
        player_name = players[player_index % len(players)]
        ball_score = play_ball(player_name)
        if ball_score == "out":
            wickets += 1
            if wickets < 10:
                print("Score:", runs, "-", wickets, "after", overs_played, "overs")
                print("Next bowler:", players[(player_index+1) % len(players)])
        else:
            runs += ball_score
        overs_played = int(player_index / len(players))
        player_index += 1
    print("Score:", runs, "-", wickets, "after", overs_played, "overs")
    return runs, wickets

# Main code
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")
players = [player1, player2]
bat_first, bowl_first = toss(player1, player2)

if bat_first == player1:
    target = 0
    print(player1, "will bat first.")
    overs = int(input("How many overs will each team play? "))
    runs, wickets = bat(target, overs, players)
    target = runs + 1
    print(player2, "needs to score", target, "runs to win.")
    overs = int(input("How many overs"))

if bat_first == player1:
    target = 0
    print(player1, "will bat first.")
    overs = int(input("How many overs will each team play? "))
    runs, wickets = bat(target, overs, players)
    target = runs + 1
    print(player2, "needs to score", target, "runs to win.")
    overs = int(input("How many overs will each team play? "))
    runs, wickets = bowl(target, overs, players)
else:
    print(player2, "will bat first.")
    target = random.choice([120, 140, 160, 180, 200])
    print("Target:", target)
    overs = int(input("How many overs will each team play? "))
    runs, wickets = bowl(target, overs, players)
    if runs < target:
        print(player1, "wins by", target - runs - 1, "runs!")
    elif runs == target:
        print("The match is tied!")
    else:
        print(player2, "wins by", 10-wickets, "wickets!")
        
        


