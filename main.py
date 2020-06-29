import random

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


def deal():
    global count
    global bot_player
    global bot_player
    global CARDS
    global DECK

    while True:
        if len(bot_player) < 2:
            card = random.choice(CARDS)
            if card in DECK:
                DECK.remove(card)
                CARDS.remove(card)
                # if card >= 2 and card <= 6:
                #     count += 1
                # elif card == 1 or card >= 10 and card <= 13: 
                #     count -= 1
                bot_player.append(card)
                cc(card)
        
        if len(bot_dealer) < 2:
            card = random.choice(CARDS)
            if card in DECK:
                DECK.remove(card)
                CARDS.remove(card)
                # if card >= 2 and card <= 6:
                #     count += 1
                # elif card == 1 or card >= 10 and card <= 13: 
                #     count -= 1
                bot_dealer.append(card)
                cc(card)
        
        if len(bot_player) == 2 and len(bot_player) == 2:
            break


def cc(card):
    global count

    if card >= 2 and card <= 6:
        count += 1
    elif card == 1 or card >= 10 and card <= 13:
        count -= 1


def option(x):
    global count
    global bot_player
    global CARDS
    global DECK
    global game

    if sum(bot_player) <= 14 or x >= 1:
        print("Count is", count)
        card = random.choice(CARDS)
        bot_player.append(card)
        DECK.remove(card)
        CARDS.remove(card)
        cc(card)
    elif sum(bot_player) == 21 or x <= 0 or sum(bot_player) >= 19:
        print("hold")
        result()


def result():
    global game

    if sum(bot_player) <= sum(bot_dealer):
        print("dealer wins:", sum(bot_dealer), " over players:", sum(bot_player))
        game = False
    elif sum(bot_player) > sum(bot_dealer):
        print("player wins:", sum(bot_player), " over dealers:", sum(bot_dealer))
        game = False



deal()
print(bot_player, count)
while game is True:
    if sum(bot_dealer) > 21:
        print("Dealer busts:", sum(bot_dealer))
        quit()
    elif sum(bot_player) > 21:
        print("Player busts:", sum(bot_player))
        game = False  # result function here
    elif sum(bot_player) == 21:
        print("hold")
        game = False  # result function here
    elif sum(bot_player) < 21:
        option(count)
        print(bot_player, "|", count, "|", sum(bot_player))
quit()