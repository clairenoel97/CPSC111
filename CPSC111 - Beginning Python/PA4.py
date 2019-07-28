#assignment 4

'''
Pass the Pigs

    a player tosses two toy pigs, each of which has a dot on one side. Each pig can land in one of six positions:
        1. on its side
            side with dot down
            side with dot up
        2. razorback
            on its back
        3. trotter
            on all 4 feet
        4. snouter
            balanced on front two feet and its snout
        5. leaning jowler
            balanced on one foot, snout, and each

    after the pigs have come to rest, the player gains or loses points based on the way pigs land:
        double (both pigs in the same position)
            sider: either both with the spot facing upward or both with the spot facing downward: 1 point
            razorback: 20 points
            trotter: 20 points
            snouter: 40 points
            jowler: 60 points
        pigout: (if both pigs are lying on their sides, one up one down)
            if this happens, the score is reset to zero
        mixed combo: a combination not mentioned about is the sum of the single pigs' scores
            pig lying on its side: 0 points
            razorback: 5 points
            trotter: 5 points
            snouter: 10 points
            jowler: 15 points

'''
import random

def display_game_rules():
    '''
    displays the game rules
    '''
    print("Welcome to Padd the Pigs")
    print("There will be two players competing until one player reaches the winning score, which will be provided by YOU!")
    print("Each players score will be determined by accumulating points after each turn\n")
    print("The first player will be chosen at random.\n")

def get_valid_winning_score():
    '''
    prompts the player for the integer number of points to play until
    must validate the number is an int
    returns the validated winning score
    '''
    winning_score = int(input("Please enter an int that represents the winning score. (Must be an int between 1 - 100): "))

    while (is_valid_winning_score(int(winning_score)) == False):
        winning_score = input("Please enter an int that represents the winning score. (Must be an int between 1 - 100): ")

    return winning_score

def is_valid_winning_score(score):
    '''
    score: int
    checks to see if the entered winning score is an int between 0-100
    returns: bool
    '''

    if score <= 0 or score > 100:
        return False
    else:
        return True

def roll_pig():
    '''
    rolls one pig
    randomly generates a pig position using the frequencies provided:
    returns a string representing the position of the pig
    '''
    rand = random.randint(1,100)

    if rand > 0 and rand <= 35:
        return "SIDE"
    elif rand > 35 and rand <= 65:
        return "SIDE-D"
    elif rand > 65 and rand <= 87:
        return "RZR"
    elif rand > 87 and rand <= 96:
        return "TROT"
    elif rand > 96 and rand <= 99:
        return "SNOUT"
    else:
        return "LEAN"

def determine_roll_result(pig1, pig2):
    '''
    determines the roll result based on the two pigs positions and returns a string representing the roll result
    '''
    if pig1 == pig2 == "SIDE":
        return "SIDER"
    elif pig1 == pig2 == "RZR":
        return "DBL-RAZR"
    elif pig1 == pig2 == "TROT":
        return "DBL-TROT"
    elif pig1 == pig2 == "SNOUT":
        return "DBL-SNOUT"
    elif pig1 == pig2 == "LEAN":
        return "DBL-LEAN"
    elif pig1 == "SIDE" and pig2 == "SIDE-D":
        return "PIGOUT"
    elif pig1 == "SIDE-D" and pig2 == "SIDE":
        return "PIGOUT"
    else:
        return "MIXED"

def choose_player():
        player1 = str(input("Please enter the name of player one: "))
        player2 = str(input("Please enter the name of player two: "))

        rand = random.randint(1,10)
        if rand % 2 == 0:
            current_player = player1
            next_player = player2
        else:
            current_player = player2
            next_player = player1
        return current_player, next_player

def calculate_total_roll_points(pig1, pig2, roll_result):
    '''
    determines the total points rolled based on the pigs positions
    returns total points
    '''
    if roll_result == "SIDER":
        return 1
    elif roll_result == "DBL-RAZR":
        return 20
    elif roll_result == "DBL-TROT":
        return 20
    elif roll_result == "DBL-SNOUT":
        return 40
    elif roll_result == "DBL-LEAN":
        return 60
    elif roll_result == "PIGOUT":
        return 0
    elif roll_result == "MIXED":
        pig1_subtotal = 0
        pig2_subtotal = 0

        if pig1 == "SIDE" or pig1 == "SIDE-D":
            pig1_subtotal += 1
        elif pig1 == "RZR":
            pig1_subtotal += 5
        elif pig1 == "TROT":
            pig1_subtotal += 5
        elif pig1 == "SNOUT":
            pig1_subtotal += 10
        else:
            pig1_subtotal += 15

        if pig2 == "SIDE" or pig2 == "SIDE-D":
            pig2_subtotal += 1
        elif pig2 == "RZR":
            pig2_subtotal += 5
        elif pig2 == "TROT":
            pig2_subtotal += 5
        elif pig2 == "SNOUT":
            pig2_subtotal += 10
        else:
            pig2_subtotal += 15

        return pig1_subtotal + pig2_subtotal

def one_turn():
    pig1 = roll_pig()
    pig2 = roll_pig()
    roll_result = determine_roll_result(pig1, pig2)
    score = calculate_total_roll_points(pig1, pig2, roll_result)
    return roll_result, score

def ask_about_players():
    players = int(input("Please enter '1' to play against the computer or '2' to play against a friend: "))

    if players == 2:
        player1, player2 = choose_player()
    else:
        player1 = str(input("Please enter the name of player one: "))
        player2 = "Computer"
    return player1, player2

def start_game():
    display_game_rules()
    winning_score = get_valid_winning_score()
    return winning_score

def change_player(current_player, player1, player2):
    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player1
    return current_player

def change_score(score, player_score):
    if score == 0:
        player_score *= score
    else:
        player_score += score
    return player_score

def main_game():
    player1_score = 0
    player2_score = 0
    play_again = 'y'

    while play_again == 'y':
        winning_score = start_game()
        player1, player2 = ask_about_players()
        current_player = player1

        while player1_score < winning_score and player2_score < winning_score:
            #current player rolls
            current_player = change_player(current_player, player1, player2)
            print()
            print(current_player + "'s turn!")
            if current_player != "Computer":
                print(input("Please press 'enter' to roll!"))
            roll_result, score = one_turn()
            print(current_player + " just rolled " + roll_result)
            if current_player == player1:
                player1_score = change_score(score, player1_score)
                print(current_player +"'s current score is: " + str(player1_score))
            else:
                player2_score = change_score(score, player2_score)
                print(current_player +"'s current score is: " + str(player2_score))

        print("\n\nGAME OVER!")
        print("The winner is: " + current_player)

        play_again = str(input("Would you like to play again? (y or n): "))
    print("Thanks for playing!")

def main():
    main_game()

main()
