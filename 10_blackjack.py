from ascii_art import blackjack_logo
import random as rm

# list of possible cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# set initial hands
def initialize_hands(deck):
    init_hands = [[0,0], [0,0]]
    init_hands[0][0] = rm.choice(deck)
    init_hands[0][1] = rm.choice(deck)
    init_hands[1][0] = rm.choice(deck)
    init_hands[1][1] = rm.choice(deck)
    return init_hands

def add_card(hand):
    hand.append(rm.choice(cards))
    return hand

def end_game(final_hands, who_won, went_over):
    print(f"\tYour final hand: {final_hands[0]}, final score: {sum(final_hands[0])}")
    print(f"\tComputer's final hand: {final_hands[1]}, final score {sum(final_hands[1])}")
    if who_won == 'draw':
        print("The game was a draw!")
    elif who_won == 'computer' and went_over:
        print("You went over. You lose \U0001F62D")
    elif who_won == 'user' and went_over:
        print(f"Opponent went over. You win \U0001F601")
    elif not went_over:
        if who_won == 'user':
            print("You have won \U0001F601")
        else:
            print("You have lost \U0001F62D")
    play_again = input("Do you want to play a game of blackjack? Tye 'y' or 'n' ")
    if play_again == 'y':
        print('\n' * 50)
        print(blackjack_logo)
        new_hand = initialize_hands(cards)
        hit_reset = ''

    return play_again, new_hand, hit_reset


# prompt user to play or not
play = input("Do you want to play a game of blackjack? Tye 'y' or 'n' ")

# print logo if the user wants to play
if play == 'y':
    print(blackjack_logo)
    hands = initialize_hands(cards)

# loop to continue while user wants to play
while play == 'y':
    # sum the cards the player has
    current_score = sum(hands[0])
    print('current score is ', current_score)
    # print the sum and the visible card the computer has
    print(f"\t\tYour cards: {hands[0]}, current score: {current_score}")
    print(f"\t\tComputer's first card: {hands[1][0]}")

    if current_score > 21:
        play, hands, hit = end_game(hands, 'computer', True)

    else:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == 'y':
            hands[0] = add_card(hands[0])
        if hit == 'n':
            went_over = False
            while sum(hands[1]) < 17:
                hands[1] = add_card(hands[1])
            if sum(hands[1]) > 21:
                winner ='user'
                went_over = True
            elif sum(hands[0]) == sum(hands[1]):
                winner = 'draw'
            elif sum(hands[0]) > sum(hands[1]):
                winner = 'user'
            else:
                winner = 'computer'
            play, hands, hit = end_game(hands, winner, went_over)
