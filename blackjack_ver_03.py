import random
from time import sleep


class Cards:
    def __init__(self, who):
        self.who = who
        self.hand = [], []

    cards = ([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
             [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

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

        print("\n" + self.who + "s hand:\n" + ", ".join(str(e) for e in self.hand[0]) + f" ({sum(self.hand[1])})")


player = Cards("Player")
dealer = Cards("Dealer")

for i in range(2):
    player.deal()
    sleep(0.7)
    dealer.deal()
    sleep(0.7)

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
    while True:
        print("\n1 - Hit"
              "\n2 - Stand\n")

        play = input("> ")

        if play == "1":
            sleep(0.7)
            player.deal()
            if sum(player.hand[1]) > 21:
                sleep(0.7)
                print("Bust!\n")
                break
        elif play == "2":
            sleep(0.7)
            print(f"\nStand. Your hands total is: {sum(player.hand[1])}\n")
            break

    if sum(player.hand[1]) < 21:
        while True:
            if sum(dealer.hand[1]) < 17:
                sleep(0.7)
                dealer.deal()
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

            if sum(dealer.hand[1]) > 21:
                sleep(0.7)
                print("\nThe dealer has bust. You win!")
                break
    elif sum(player.hand[1]) == 21:
        print("")
    else:
        sleep(0.7)
        print("\nBetter luck next time!")

