from art import logo
import random


def check_new_card(player_hand):
    total_score = sum(player_hand)
    if total_score > 21:
        return False
    return True


def check_player_wining(player_hand, computer_hand):
    if not check_new_card(player_hand):
        return False
    player_total = sum(player_hand)
    computer_total = sum(computer_hand)
    if player_total > computer_total:
        return True
    else:
        return False


def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_card = [random.choice(cards), random.choice(cards)]
    player_card = [random.choice(cards), random.choice(cards)]
    print("your card is: ", player_card)
    print(f"dealer's first card is: {dealer_card[0]}")
    continuing = True
    while continuing:
        pass_or_deal = input("Type 'p' to pass or 'd' to deal: ")
        if pass_or_deal == "d":
            player_card.append(random.choice(cards))
            print("your card is: ", player_card)
            continuing = check_new_card(player_card)
        else:
            continuing = False
    print("your final hand is: ", player_card)
    print("Computer final hand : ", dealer_card)
    is_player_winning = check_player_wining(player_hand=player_card, computer_hand=dealer_card)
    if is_player_winning:
        print("you won!")
    else:
        print("you lost!")
    if input("Do you want to play a game of Blackjack? (y/n)") == 'y':
        play_blackjack()


print(logo)
play_blackjack()