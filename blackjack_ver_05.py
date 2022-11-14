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

    cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    dict = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }

    def deal(self, show_first_card):
        new_card = str(random.choice(self.cards))
        new_value = self.dict[new_card]

        self.hand[0].append(new_card)
        self.hand[1].append(new_value)

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
                print("\n" + self.who + "s hand:\nX, " + ", ".join(str(e) for e in self.hand[0][1:]))


# dokumentirati...
class Betting:
    def __init__(self, balance):
        self.balance = balance

    def betting(self, bet):
        self.balance -= int(bet)
        self.print_balance()

    def lose(self):
        self.print_balance()

    def push(self, bet):
        self.balance += bet
        self.print_balance()

    def win(self, bet):
        self.balance += (bet * 2)
        self.print_balance()

    def print_balance(self):
        print(f"\nPlayer balance is: {str(self.balance)}")


# petlja za upis uloga
while True:
    try:
        balance = int(input("Buy in: "))
        game = Betting(balance)
        break
    except Exception as e:
        print(e)

# glavna petlja ruke
while True:

    # ovo je petlja za upis beta manjeg ili jednakog balansu
    while True:

        # petlja za ispravan upis bet-a
        while True:
            try:
                bet = int(input("\nTake a bet: "))
                break
            except Exception as e:
                print(e)

        if bet > 0:
            if int(bet) <= game.balance:
                game.betting(bet)
                break
            else:
                print(f"\nCan't bet higher than balance!\nPlayer balance is: {game.balance}")
        else:
            print("Bet must be larger than zero!")

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
        game.push(bet)
    elif sum(player.hand[1]) == 21:
        sleep(0.7)
        print("\nBlackjack!")
        game.win(bet)
    elif sum(dealer.hand[1]) == 21:
        sleep(0.7)
        print("\nThe dealer has Blackjack! You lose!")
        game.lose()
    else:
        # igra player
        while True:  # petlja samo za ruku koja se igra
            sleep(0.7)
            print("\n1 - Hit"
                  "\n2 - Stand\n")

            play = input("> ")

            if play == "1":
                sleep(0.7)
                player.deal(True)
                if sum(player.hand[1]) > 21:
                    sleep(0.7)
                    print("\nBust!\n")
                    game.lose()
                    break
            elif play == "2":
                sleep(0.7)
                print(f"\nStand. Your hands total is: {sum(player.hand[1])}\n")
                break

        if sum(player.hand[1]) <= 21:
            # ispisuju prve dvije karte dealera
            sleep(0.7)
            print("\n" + "Dealers hand:\n" + ", ".join(str(e) for e in dealer.hand[0]) + f" ({sum(dealer.hand[1])})")
            # igra dealer
            while True:
                if sum(dealer.hand[1]) < 17:
                    sleep(0.7)
                    dealer.deal(True)
                elif 17 <= sum(dealer.hand[1]) <= 21:
                    if sum(dealer.hand[1]) < sum(player.hand[1]):
                        sleep(0.7)
                        print(f"\nThe dealer has {sum(dealer.hand[1])}. You win!")
                        game.win(bet)
                        break
                    elif sum(dealer.hand[1]) > sum(player.hand[1]):
                        sleep(0.7)
                        print(f"\nThe dealer has {sum(dealer.hand[1])}. You lose!")
                        game.lose()
                        break
                    elif sum(dealer.hand[1]) == sum(player.hand[1]):
                        sleep(0.7)
                        print(f"\nThe dealer has {sum(dealer.hand[1])}. Player is pushed!")
                        game.push(bet)
                        break
                elif sum(dealer.hand[1]) > 21:
                    sleep(0.7)
                    print("\nThe dealer has bust. You win!")
                    game.win(bet)
                    break
        elif sum(player.hand[1]) == 21:
            print("")

    # ako je balans = nula
    if game.balance == 0:
        print("\nOut of funds!")
        break
    else:
        print("\n1 - Bet"
              "\n2 - Quit\n")

        play = input("> ")
        if play == "2":
            break

print("\nGame over!")
