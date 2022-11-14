import random
from time import sleep


#
# klasa Cards:
# dijeli karte i ispisuje ih
#
class Cards:
    def __init__(self, who):
        self.who = who
        self.hand = [], []

    cards = ([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
             [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

    def deal(self, show_first_card):
        self.hand[1].clear()

        # kontrola cetiri karte
        # self.hand[0].append(random.choice(self.cards[0]))
        new_card = random.choice(self.cards[0])
        self.hand[0].append(new_card)

        for i in range(0, len(self.hand[0])):
            counter = int(self.cards[0].index(self.hand[0][i]))
            self.hand[1].append(self.cards[1][counter])

        if "A" in self.hand[0] and sum(self.hand[1]) > 21:
            while sum(self.hand[1]) > 21 and 11 in self.hand[1]:
                self.hand[1].remove(11)
                self.hand[1].insert(0, 1)

        if show_first_card:
            print("\n" + self.who + "s hand:\n" + ", ".join(str(e) for e in self.hand[0]) + f" ({sum(self.hand[1])})")
        else:
            if len(self.hand[0]) == 1:
                print("\n" + self.who + "s hand:\n X")
            else:
                print("\n" + self.who + "s hand:\n X, " + ", ".join(str(e) for e in self.hand[0][1:]))


class Betting:
    def __init__(self, balance):
        self.balance = balance

    def betting(self, bet):
        self.balance -= int(bet)


balance = int(input("> "))
betting = Betting(balance)
print(str(betting.balance))

while True: # glavna petlja cijele igre

    bet = int(input("> "))
    # ne smije biti veći od trenutnog stanja
    betting.betting(bet)
    print(str(betting.balance))

    # kreiraju se objekti player i dealer
    player = Cards("Player")
    dealer = Cards("Dealer")



    # dajem prve dvije karte
    for i in range(2):
        player.deal(True)
        sleep(0.7)
        dealer.deal(False)
        sleep(0.7)

    # provjerava se blackJack
    if sum(player.hand[1]) == 21 and sum(dealer.hand[1]) == 21:
        sleep(0.7)
        print("\nBoth the dealer and the player have Blackjack! Player is pushed!")
    elif sum(player.hand[1]) == 21:
        sleep(0.7)
        print("\nBlackjack!")
    elif sum(dealer.hand[1]) == 21:
        sleep(0.7)
        print("\nThe dealer has Blackjack! You lose!")
    else:
        # igra player
        while True: # petlja samo za ruku koja se igra
            print("\n1 - Hit"
                  "\n2 - Stand\n")

            play = input("> ")

            if play == "1":
                sleep(0.7)
                player.deal(True)
                if sum(player.hand[1]) > 21:
                    sleep(0.7)
                    print("Bust!\n")
                    break
            elif play == "2":
                sleep(0.7)
                print(f"\nStand. Your hands total is: {sum(player.hand[1])}\n")
                break

        # ispisuju prve dvije karte dealera
        print("\n" + "Dealers hand:\n" + ", ".join(str(e) for e in dealer.hand[0]) + f" ({sum(dealer.hand[1])})")
        # provjera se je li gotovo

        if sum(player.hand[1]) < 21:
            # igra dealer
            while True:
                if sum(dealer.hand[1]) < 17:
                    sleep(0.7)
                    dealer.deal(True)
                elif 17 <= sum(dealer.hand[1]) <= 21:
                    if sum(dealer.hand[1]) < sum(player.hand[1]):
                        sleep(0.7)
                        print(f"\nThe dealer has {sum(dealer.hand[1])}. You win!")
                        break
                    elif sum(dealer.hand[1]) > sum(player.hand[1]):
                        sleep(0.7)
                        print(f"\nThe dealer has {sum(dealer.hand[1])}. You lose!")
                        break
                    elif sum(dealer.hand[1]) == sum(player.hand[1]):
                        sleep(0.7)
                        print(f"\nThe dealer has {sum(dealer.hand[1])}. Player is pushed!")
                        break
                elif sum(dealer.hand[1]) > 21:
                    sleep(0.7)
                    print("\nThe dealer has bust. You win!")
                    break
        elif sum(player.hand[1]) == 21:
            print("")
        else:
            sleep(0.7)
            print("\nBetter luck next time!")

    print("\n1 - Bet"
          "\n2 - Quit\n")

    play = input("> ")
    if play == "2":
        break
