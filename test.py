import random
from time import sleep


class Cards:
    def __init__(self, who):
        self.who = who
        self.hand = [], []

    # cards = (["6", "7", "8", "A"],
    #          [6, 7, 8, 11])

    cards = ([4, 5, 6, 7, 8, 9, 10, "J", "A", "A", "A"],
             [4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 11])

    def deal(self):
        self.hand[1].clear()
        self.hand[0].append(random.choice(self.cards[0]))

        for i in range(0, len(self.hand[0])):
            counter = int(self.cards[0].index(self.hand[0][i]))
            self.hand[1].append(self.cards[1][counter])

        if "A" in self.hand[0] and sum(self.hand[1]) > 21:
            while sum(self.hand[1]) > 21 and 11 in self.hand[1]:
                self.hand[1].remove(11)
                self.hand[1].insert(0, 1)

        if self.who == "Player":
            print("\n" + self.who + "s hand:\n" + ", ".join(str(e) for e in self.hand[0]) + f" ({sum(self.hand[1])})")
        else:
            print("\n" + self.who + "s hand:\n" + "X, " + str(self.hand[0][0]))
            print(self.hand[0])


player = Cards("Player")
dealer = Cards("Dealer")

for i in range(2):
    player.deal()
    sleep(0.5)
    dealer.deal()
    sleep(0.5)

if sum(player.hand[1]) == 21 and sum(dealer.hand[1]) == 21:
    sleep(1)
    print("\nBoth the dealer and the player have Blackjack! Player is pushed!")
elif sum(player.hand[1]) == 21:
    sleep(1)
    print("\nBlackjack!")
elif sum(dealer.hand[1]) == 21:
    sleep(1)
    print("\nThe dealer has Blackjack! You lose!")
else:
    while True:
        print("\n1 - Hit"
              "\n2 - Stand\n")

        play = input("> ")

        if play == "1":
            sleep(1)
            player.deal()
            if sum(player.hand[1]) == 21:
                sleep(1)
                print("Blackjack!")
                break
            elif sum(player.hand[1]) > 21:
                sleep(1)
                print("Bust!\n")
                break
        elif play == "2":
            sleep(1)
            print(f"\nStand. Your hands total is: {sum(player.hand[1])}\n")
            break

    if sum(player.hand[1]) < 21:
        while True:
            if sum(dealer.hand[1]) < 17:
                sleep(1)
                dealer.deal()
            elif 17 <= sum(dealer.hand[1]) <= 21:
                if sum(dealer.hand[1]) < sum(player.hand[1]):
                    sleep(1)
                    print(f"\nThe dealer had {sum(dealer.hand[1])}. You win!")
                    break
                if sum(dealer.hand[1]) >= sum(player.hand[1]):
                    sleep(1)
                    print(f"\nThe dealer had {sum(dealer.hand[1])}. You lose!")
                    break
            if sum(dealer.hand[1]) > 21:
                sleep(1)
                print("\nThe dealer has bust. You win!")
                break
    elif sum(player.hand[1]) == 21:
        print("")
    else:
        sleep(1)
        print("\nBetter luck next time!")
