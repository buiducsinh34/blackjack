'''
BlackJack - simple version
Author: Sinh Bui
Date: October-10-2018
'''
import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return f'Card {self.value} with {self.color}'

class Dealer:
    def __init__(self, cards, total_points, count):
        self.cards = cards
        self.total_points = total_points
        self.count = count
    def __str__(self):
        return f'Dealer has {self.total_points} points'
    def pointsUpdate(self):
        aces = 0
        self.total_points = 0
        for c in self.cards:
            if c.value != 1:
                if c.value < 10:
                    self.total_points += c.value
                else:
                    self.total_points += 10
            else:
                aces += 1
        while aces != 0:
            if self.total_points < 12:
                self.total_points += 10
            else:
                self.total_points += 1
            aces -= 1


class Player:
    def __init__(self, cards, total_points, balance, count):
        self.count = count
        self.cards = cards
        self.total_points = total_points
        self.balance = balance
    def __str__(self):
        return f'Player has {self.total_points} points and ${self.balance}'
    def pointsUpdate(self):
        aces = 0
        self.total_points = 0
        for c in self.cards:
            if c.value != 1:
                if c.value < 10:
                    self.total_points += c.value
                else:
                    self.total_points += 10
            else:
                aces += 1
        while aces != 0:
            if self.total_points < 12:
                self.total_points += 10
            else:
                self.total_points += 1
            aces -= 1

def cardPrintOut(print_everything):
    if print_everything:
        dealer_print = f"{dealer.cards[0]}\t"
    else:
        dealer_print = "First card\t"
    player_print = ""
    for c in dealer.cards[1:]:
        dealer_print += f"{c}\t"
    for c in player.cards:
        player_print += f"{c}\t"
    print(dealer_print)
    print(player_print)

def askIfContinue():
    print(f"Your balance is: ${player.balance}")
    ans = input("Do you want to play another game? (Y/N)")
    if ans.lower() in ["y","yes"]:
        gameReset()
        return True
    else:
        print("Hope you enjoyed the time playing this game, and see you next time!")
        return False

def gameReset():
    player.cards = []
    player.total_points = 0
    player.count = 0
    dealer.cards = []
    dealer.total_points = 0
    dealer.count = 0
    deck = [Card(value, color) for value in range(1, 14) for color in colors]
    random.shuffle(deck)

colors = ['hearts', 'diamonds', 'spades', 'clubs']
deck = [Card(value, color) for value in range(1, 14) for color in colors]
random.shuffle(deck)

dealer = Dealer([], 0, 0)
player = Player([], 0, 1000, 0)
print(f"You have ${player.balance}")


while True:
    try:
        bet = int(input('Please enter your bet amount($): '))
    except:
        print('Please enter a number')
        continue
    if bet > player.balance:
        print('Sorry, but you cannot bet more than what you have')
        continue
    else:
        print(f"You have bet ${bet}, let's begin!")

    player.cards.append(deck.pop())
    dealer.cards.append(deck.pop())

    player.cards.append(deck.pop())
    dealer.cards.append(deck.pop())

    cardPrintOut(False)

    playing = True
    player_busted = False


    while (playing == True) and (player.count < 3):
        ans = input("Do you want to take another card? (Y/N)")
        if ans.lower() in ["y","yes"]:
            player.count += 1
            player.cards.append(deck.pop())
            cardPrintOut(False)
            player.pointsUpdate()
        else:
            player.pointsUpdate()
            playing = False
        if player.total_points > 21:
            playing = False
            player_busted = True
    if player_busted == True:
        player.balance -= bet
        print("You have busted!")
        print(f"\nyour points: {player.total_points}, dealer's points: {dealer.total_points}")            
        if askIfContinue():
            continue
        else:
            break
    
    dealer.pointsUpdate()
    while (dealer.total_points < player.total_points) and (dealer.total_points < 21) and (dealer.count < 3):
        dealer.cards.append(deck.pop())
        dealer.pointsUpdate()
        print(dealer.total_points)
        cardPrintOut(False)
    
    if dealer.total_points > 21:
        print("Dealer's busted, you've won!")
        print(f"\nyour points: {player.total_points}, dealer's points: {dealer.total_points}")
        cardPrintOut(True)
        player.balance += bet
        if askIfContinue():
            continue
        else:
            break
    elif dealer.total_points < player.total_points:
        print("You've won!")
        print(f"\nyour points: {player.total_points}, dealer's points: {dealer.total_points}")
        cardPrintOut(True)
        player.balance += bet
        if askIfContinue():
            continue
        else:
            break
    else:
        print("You've lost!")
        print(f"\nyour points: {player.total_points}, dealer's points: {dealer.total_points}")
        cardPrintOut(True)
        player.balance -= bet
        if askIfContinue():
            continue
        else:
            break