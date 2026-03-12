import random
from termcolor import colored

#starting 
print(colored("\nHello, this is a baby version of blackjack\n", "light_grey"))

#deck
cards = ["1","2","3","4","5","6","7","8","9","10"]*4
random.shuffle(cards)

#dealer and player cards "hands"
player_hand = []
dealer_hand = []

#code comands
def count(name_hand):
    sumary = 0
    for card in name_hand:
        sumary = sumary + int(card)
    return sumary

def take_card(name_hand):
    try:
        name_hand.append(cards[0])
        del cards[0]
    except:
        print(colored("Fire started end all cards burned so we can`t end our game.", "light_red"))
        exit()

def show_all_hands():
    print(colored("Your cards:", "green"), *player_hand)
    print(colored("Dealer:", "red"), f"{dealer_hand[0]} ?")

def check_hand():
    if count(player_hand) > 21:
        print("You lost.")
        return True
    elif count(player_hand) == 21:
        print("You won!!!")
        return True
    elif count(dealer_hand) > 21:
        print("You won!!!")
        return True
    elif count(dealer_hand) == 21:
        print("You lost.")
        return True
    return False




#dealer and player takes two cards
take_card(player_hand)
take_card(player_hand)
take_card(dealer_hand)
take_card(dealer_hand)
print("Dealer gived you a card\nDealer taked a card")
print("Dealer gived you a card\nDealer taked a card\n")
show_all_hands()

#loop for game
while check_hand() != True:

    #player move
    player_move = input("\nYour move>")
    if player_move == "hit":
        take_card(player_hand)
        print("You taked the card")

    elif player_move == "stand":
        while count(dealer_hand) < 17:
            take_card(dealer_hand)
        print(colored("Your cards:", "green"), *player_hand)
        print(colored("Dealer:", "red"), *dealer_hand)

        player_end = count(player_hand)
        dealer_end = count(dealer_hand)

        if player_end > dealer_end and player_end <= 21:
            print(colored("You won!!!"))
            break
        elif player_end < dealer_end and dealer_end <= 21:
            print(colored("You lost\nDo you want to play another one?"))
            break
        elif player_end == dealer_end:
            print("Tie\nTry again next one you gonna win.")
            break
        
    else:
        print("What? say again pls.")  

    print()#this is just for enter          
    show_all_hands()