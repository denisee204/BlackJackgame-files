from random import shuffle

class Hand(list):
    'A hand for Black Jack that is a list of cards'
    cards = []
def evalhd(self):
    'Gets highest value of hand under 21'
    aces = 0
    value = 0
    for card in self:
        if card[0] == 1:
            aces = aces+1
            value = value + 11
        elif card[0] >= 10:
            value = value + 10
        else:
            value = value + card[0]
    while value > 21 and aces > 0:
        value = value - 10
        aces = aces -1
    return value


class Deck(list):
    'A deck of cards as a list'
    cards = []


# class Card:
#     'A card represented by rank and suit'
#     def __init__(self, rank, suit):
#         assert rank in range(1, 14) and suit in range(4)
#         self.rank = rank
#         self.suit = suit
#     def rankSuittoString(self):
#         #here we are defining the ranks as strings
#         if (self.rank == 0):
#             rankString= "Ace"
#         elif (self.rank == 1):
#             rankString= "Ace"
#         elif (self.rank == 2):
#             rankString= "Two"
#         elif (self.rank == 3):
#             rankString= "Three"
#         elif (self.rank == 4):
#             rankString= "Four"
#         elif (self.rank == 5):
#             rankString= "Five"
#         elif (self.rank == 6):
#             rankString= "Six"
#         elif (self.rank == 7):
#             rankString= "Seven"
#         elif (self.rank == 8):
#             rankString= "Eight"
#         elif (self.rank == 9):
#             rankString= "Nine"
#         elif (self.rank == 10):
#             rankString= "Ten"
#         elif (self.rank == 11):
#             rankString= "Jack"
#         elif (self.rank == 12):
#             rankString= "Queen"
#         elif (self.rank == 13):
#             rankString= "King"
#         else:
#             rankString=str(self.rank)
#             #Now we define the suits as strings
#         if (self.suit== 0):
#             suitString= "Spade"
#         elif(self.suit== 1):
#             suitString= "Heart"
#         elif(self.suit== 2):
#             suitString= "Diamond"
#         elif(self.suit== 3):
#             suitString= "Club"
#         else:
#             suitString=str(self.suit)
#         return(suitString + "_" + rankString + "_RA.gif")

class Scores:
    'Scores for the dealer and the player in the Black Jack game'
    def __init__(self):
        self.player = 0
        self.dealer = 0
    def dealerWon(self):
        self.dealer = self.dealer + 1
    def playerWon(self):
        self.player = self.player + 1



class BlackJack :
    'Object to hold status of play in Black Jack'
    endGame = 1
    playerWon = 2
    dealerWon = 3
    tie = 4
    startHand = 0
    def __init__(self):
        'create the deck of cards and initialize the game for dealer and player'
        deck = []
        # Create 4 suits with 13 cards in each suit
        for suit in range(4):
            for value in range(1,14):
                deck.append([value, suit])
        #print(deck)
        shuffle(deck)
        print('great')
        self.scores = Scores()
        self.dealer = []
        self.player = []
        self.deck = deck
        self.status = self.startHand
        self.test = False

    def play(self):
        'Plays until deck is empty'
        while True:
            self.playHand()
            if self.status == self.endGame:
                break
            self.whoWon()
            if self.status == self.playerWon:
                self.scores.playerWon()
            elif self.status == self.dealerWon:
                self.scores.dealerWon()
            self.show('=============================================')
            stat = ['Start hand', 'End game', 'Player won', 'Dealer won', 'Tie']
            self.show(stat[self.status])
            self.displayHands()
            self.displayDealerHand()
            self.dealer = []
            self.player = []
            self.status = self.startHand
        self.show('Player score is ' + str(self.scores.player))
        self.show('Dealer score is ' + str(self.scores.dealer))

    def playHand(self):
        'Play one hand'
        self.deal2()
        self.deal2dealer()
        if self.winWith2():
            return
        if self.winWith2Dealer():
            return
        if self.status == self.endGame:
            return
        self.playerChoice()
        if self.status == self.endGame:
            return
        if evalhd(self.player) > 21:
            return
        self.dealerStrategy()
#deal for the dealer
    def deal2dealer(self):
        'Deals two cards to player and dealer if there are 4 cards.'
        if len(self.deck) >= 4:
            # self.show('===Starting new hand===')
            for i in range(2):
                self.deal1(self.dealer)
            self.displayDealerHand()
            strings=[]
            for card in self.dealer:
                strings.append(str(card[1]))
            return strings

#this section is for the player
    def deal2(self):
        'Deals two cards to player and dealer if there are 4 cards.'
        if len(self.deck) >= 4:
            self.show('===Starting new hand===')
            for i in range(2):
                self.deal1(self.player)
            self.displayHands()
            strings= []
            for card in self.player:
                strings.append(str(card[1]))
            return strings


        else:
            self.show('===Game Over===')
            self.status = self.endGame

    def deal1(self,hand):
        'Adds a card from deck onto the hand. Sets status if out of cards.'
        if len(self.deck) > 0:
            #print (hand)
            hand.append(self.deck.pop())
        else:
            self.status = self.endGame

    def playerChoice(self):
        'Asks user to choose to stand or take a hit and takes action. Detects end of game.'
        #print(self.player)
        self.deal1(self.player)
        # self.player.append(card1)
        print ('self.player')
        print(self.player)
        # return self.player
        # print(self.player)
        strings= []
        for card in self.player:
            strings.append((card[0:2]))
            # print('strings'+ strings)
        return strings
        if evalhd(self.player)>21:
            self.status == self.dealerWon
        if self.status == self.endGame:
            return

    def playerstand(self):
        if self.status == self.endGame:
            return
    def dealerStrategy(self):
        'Adds cards if dealer hand is less than 18'
        print('dealer hand ='+ str(self.dealer))
        if evalhd(self.dealer) < 21:
            if evalhd(self.dealer) <= 17:
                self.deal1(self.dealer)
                strings= []
                for card in self.dealer:
                    strings.append((card[0:2]))
                return strings
            if self.status == self.endGame:
                return
            # self.show(displayDealerHand())
        else:
            return

    def whoWon(self):
        'Uses higher hand to determine winner.'
        valued = evalhd(self.dealer)
        valuep = evalhd(self.player)
        if valued > 21:
            self.status = self.playerWon
        elif valuep > 21:
            self.status = self.dealerWon
        elif valued == valuep:
            self.status = self.tie
        elif valued > valuep:
            self.status = self.dealerWon
        else:
            self.status = self.playerWon

    def displayHands(self):
        'Displays the Player hand'
        suits = ['\u2660', '\u2661', '\u2662', '\u2663']
        ranks = ['A', 2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.show("Player")
        for card in self.player:
            self.show(card)
        self.show('Hand value ' + str(evalhd(self.player)))

    def displayDealerHand(self):
        'Displays the Dealer hand'
        # Here we have separated the dealer hand in order to display it at the end rather than at the same time as the player.
        suits = ['\u2660', '\u2661', '\u2662', '\u2663']
        ranks = ['A', 2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.show("Dealer")
        for card in self.dealer:
            self.show(card)
        self.show('Hand value ' + str(evalhd(self.dealer)))

    def winWith2(self):
        'Handles getting 21 on first two cards'
        strings= []
        for card in self.player:
            strings.append(str(card[1]))
        for card in self.dealer:
            strings.append(str(card[1]))
        if evalhd(self.player)== 21:
            self.displayHands()
            self.displayDealerHand()
            return True
        else:
            return False
    def winWith2Dealer(self):
        strings=[]
        for card in self.dealer:
            strings.append(str(card[1]))
        if evalhd(self.dealer) == 21:
            self.displayHands()
            self.displayDealerHand()
            return True
        else:
            return False


    def show(self,v):
        'Shows the argument to the user. unless testing.'
        if self.test:
            return
        print(v)

    def getInput(self,strg):
        'Uses standard input unless testing. Random selection in testing.'
        if not(self.test):
            return(input(strg))
        else:
            choice = ['h','','k','h','','h','','h','']
            shuffle(choice)
            return choice[0]
