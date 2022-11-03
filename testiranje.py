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
    print("Dealers hand:\n" + ", ".join(str(e) for e in dealer_hand[0]))
    print("Players hand:\n" + ", ".join(str(e) for e in player_hand[0]))


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

while True:
    print("\n1 - Hit"
          "\n2 - Stand\n")

    play = input("> ")

    if play == "1":
        player_hand[0].append(random.choice(cards[0]))
        player_hand_value()
        print_cards()
        print(sum(player_hand[1]))
        if sum(player_hand[1]) > 21:
            print("Bust!\n")
            break
    elif play == "2":
        print(f"Stand. Your hands total is: {sum(player_hand[1])}\n")
        break

if sum(player_hand[1]) < 21:
    petlja za dilera
    while True:

        print(dealer_hand[1])
        print(sum(dealer_hand[1]))
        print("////////////")

        if 17 < sum(dealer_hand[1]) < 21:


        elif sum(dealer_hand[1]) < 17:
            dealer_hand[0].append(random.choice(cards[0]))
            dealer_hand_value()

            if sum(dealer_hand[1]) < sum(player_hand[1]):
                print(dealer_hand[0])
                print(sum(dealer_hand[1]))
                print("You win!")
                break
            if sum(dealer_hand[1]) >= sum(player_hand[1]):
                print(dealer_hand[0])
                print(sum(dealer_hand[1]))
                print("You lose! Better luck next time...")
                break
        else:
            print(dealer_hand[0])
            print(sum(dealer_hand[1]))
            print("The dealer bust. You win!")
            break