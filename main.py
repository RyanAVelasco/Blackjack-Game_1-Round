import random
import time

CARDS = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13   
]
DECK = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13   
]

bot_player = []
bot_dealer = []
game = True
count = 0
money_dealer = 1000
money_player = 100
pot = 0


def result(x):
    global money_player
    global money_dealer

    if x == "win":
        money_dealer -= pot
        money_player += pot
        return "Player wins: " + str(pot)
    elif x == "lose":
        money_dealer -= pot
        money_player += pot
        return "Dealer wins: " + str(pot)


def draw():
    global count 

    card = random.choice(CARDS)

    if card in DECK:
        DECK.remove(card)
        CARDS.remove(card)
        # print(DECK)
        if card >= 2 and card <= 6:
            count += 1
        elif card == 1 or card >= 10 and card <= 13: 
            count -= 1
    
    # if count >= 1:
    #     print(count, card, "hit")
    # elif count <= 0:
    #     print(count, card, "hold/stay")
        
    if not CARDS:
        print("No more cards in deck")
        quit()

    return card


def hold():
    global bot_player
    global bot_dealer

    if sum(bot_player) < sum(bot_dealer):
        result("win")
    else:
        result("lose")


def CountTally():
    global count 

    card = random.choice(CARDS)
    if card in DECK:
        DECK.remove(card)
        CARDS.remove(card)
        print(DECK)
        if card >= 2 and card <= 6:
            count += 1
        elif card == 1 or card >= 10 and card <= 13: 
            count -= 1
    
    # if count >= 1:
    #     print(count, card, "hit")
    # elif count <= 0:
    #     print(count, card, "hold/stay")
        
    if not CARDS and not DECK:
        print("No more cards in deck")
        quit()
        

def game():        
    global bot_player
    global bot_dealer
    
    while True:
        bot_player.append(draw())
        bot_player.append(draw())
        bot_dealer.append(draw())
        bot_dealer.append(draw())

        if sum(bot_player) <= 21 or sum(bot_dealer) <= 21: 
            print(bot_player, "=", sum(bot_player), "-", "Count: ", count)
            print(bot_dealer, "=", sum(bot_dealer))

            if count > 0:
                print("Player hits at: " + str(sum(bot_player)))
                bot_player.append(draw())
            else:
                print("Player holds at: " + str(sum(bot_player)))
                hold()
        else:
            continue

            


game()

    # CountTally()
# elif card not in DECK:
#     print("Not in deck")