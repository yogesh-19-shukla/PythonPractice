import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
    
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def dealCard(self, number):
        cards_dealt = []
        for i in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card) 
        return cards_dealt

class Hand:
      def __init__(self, dealer=False):
          self.cards = []
          self.value = 0
          self.dealer = dealer

      def addCard(self, cardList):
              self.cards.extend(cardList) 

      def calculateValue(self): 
          self.value = 0
          has_ace = False

          for card in self.cards: 
              card_value = int(card.rank["value"])
              self.value += card_value
              if card.rank["rank"] == "A":
                  has_ace = True
          if has_ace and self.value > 21:
              self.value -= 10              

      def getValue(self):
          self.calculateValue()
          return self.value
      
      def isBlackJack(self):
          return self.getValue() == 21
      
      def display(self, dealerCards=False):
          print (f'''{"Dealer's" if self.dealer else "Your"} hand:''')
          for index, card in enumerate(self.cards):
              if self.dealer and index == 0 and not dealerCards and not self.isBlackJack():
                  print ("Hidden card")
              else:
                print (card)

          if not self.dealer:
              print (f"Total value: {self.getValue()}")    

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games would you like to play? "))
            except ValueError:
                print("Please enter a valid number.")
        while game_number < games_to_play:
            game_number += 1 
            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.addCard(deck.dealCard(1))
                dealer_hand.addCard(deck.dealCard(1)) 

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()          

    def checkWinner(self, player_hand, dealer_hand):
        player_value = player_hand.getValue()
        dealer_value = dealer_hand.getValue()

        if player_value > 21:
            return "Dealer wins! You busted."
        elif dealer_value > 21:
            return "You win! Dealer busted."
        elif player_hand.isBlackJack():
            return "You win!"
        elif dealer_hand.isBlackJack():
            return "Dealer wins!"
        else:
            return "It's a tie!"
