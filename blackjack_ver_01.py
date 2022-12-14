import random

cards = ([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
         [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

player_hand = [], []
dealer_hand = [], []


def deal():
    dealer_hand[0].extend([random.choice(cards[0]), random.choice(cards[0])])
    player_hand[0].extend([random.choice(cards[0]), random.choice(cards[0])])

    for i in range(0, len(player_hand[0])):
        counter = int(cards[0].index(player_hand[0][i]))
        player_hand[1].append(cards[1][counter])

    for i in range(0, len(dealer_hand[0])):
        counter = int(cards[0].index(dealer_hand[0][i]))
        dealer_hand[1].append(cards[1][counter])


def print_cards():
    print("\nDealers hand:\n" + ", ".join(str(e) for e in dealer_hand[0]) + f" ({sum(dealer_hand[1])})")
    print("\nPlayers hand:\n" + ", ".join(str(e) for e in player_hand[0]) + f" ({sum(player_hand[1])})")


def player_hand_value():
    player_hand[1].clear()
    for i in range(0, len(player_hand[0])):
        counter = int(cards[0].index(player_hand[0][i]))
        player_hand[1].append(cards[1][counter])


def dealer_hand_value():
    dealer_hand[1].clear()
    for i in range(0, len(dealer_hand[0])):
        counter = int(cards[0].index(dealer_hand[0][i]))
        dealer_hand[1].append(cards[1][counter])


deal()
print_cards()

if sum(player_hand[1]) == 21:
    print("\nBlackjack!")
elif sum(dealer_hand[1]) == 21:
    print("\nThe dealer has Blackjack! You lose!")
else:
    while True:
        print("\n1 - Hit"
              "\n2 - Stand\n")

        play = input("> ")

        if play == "1":
            player_hand[0].append(random.choice(cards[0]))
            player_hand_value()
            print_cards()
            if sum(player_hand[1]) == 21:
                print("Blackjack!")
                break
            elif sum(player_hand[1]) > 21:
                print("Bust!\n")
                break
        elif play == "2":
            print(f"\nStand. Your hands total is: {sum(player_hand[1])}\n")
            break

    if sum(player_hand[1]) < 21:
        while True:
            if sum(dealer_hand[1]) < 17:
                dealer_hand[0].append(random.choice(cards[0]))
                dealer_hand_value()
                print("\nDealers hand:\n" + ", ".join(str(e) for e in dealer_hand[0]) + f" ({sum(dealer_hand[1])})")
            elif 17 <= sum(dealer_hand[1]) <= 21:
                if sum(dealer_hand[1]) < sum(player_hand[1]):
                    print(f"\nThe dealer had {sum(dealer_hand[1])}. You win!")
                    break
                if sum(dealer_hand[1]) >= sum(player_hand[1]):
                    print(f"\nThe dealer had {sum(dealer_hand[1])}. You lose!")
                    break
            if sum(dealer_hand[1]) > 21:
                # print("\nDealers hand:\n" + ", ".join(str(e) for e in dealer_hand[0]))
                print("\nThe dealer has bust. You win!")
                break
    else:
        print("\nend")
