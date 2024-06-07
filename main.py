from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def play_game():
    clear()
    print(logo)
    another_card = True
    player_hand = random.sample(cards, 2)
    player_score = sum(player_hand)
    computer_hand = random.sample(cards, 2)
    computer_score = sum(computer_hand)
    while computer_score < 17:
        computer_hand.extend(random.sample(cards,1))
        computer_score = sum(computer_hand)
        if 11 in computer_hand and sum(computer_hand) > 21:
            computer_hand.remove(11) 
            computer_hand.append(1)
            computer_score = sum(computer_hand)
    if computer_score >= 21 or player_score == 21:
        another_card = False
    while another_card:
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        if input("Type 'y' to get another card, type 'n' to pass:") == 'y':
            player_hand.extend(random.sample(cards,1))
            if 11 in player_hand and sum(player_hand) > 21:
                player_hand.remove(11) 
                player_hand.append(1)
            player_score = sum(player_hand)
            if player_score >= 21:
                another_card = False  
        else:
            another_card = False
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    if player_score > 21 and computer_score > 21:
        print("Both players went over. It's a draw")
    elif player_score > 21:
        print("You went over. You lose")
    elif computer_score > 21:
        print("Opponent went over. You win")
    elif player_score < computer_score and computer_score == 21:
        print("You lose, Computer has a BlackJack")
    elif player_score < computer_score:
        print("You lose")
    elif player_score > computer_score and player_score == 21:
        print("Its a BlackJack, you Win")
    elif player_score > computer_score:
        print("You win")
    else:
        print("It's a draw")
    
while input("Do you want to play a game of BlackJack? Type 'y' or 'n':") == 'y':
    play_game()      
