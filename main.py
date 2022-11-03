import random

cards = ([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

player_hand = [], []
dealer_hand = [], []

def deal():
    dealer_hand[0].extend([random.choice(cards[0]), random.choice(cards[0])])
    player_hand[0].extend([random.choice(cards[0]), random.choice(cards[0])])

def print_cards():
    print("Dealers hand:\n" + ", ".join(str(e) for e in dealer_hand[0]))
    print("Players hand:\n" + ", ".join(str(e) for e in player_hand[0]))

def player_hand_value():
    player_hand[1].clear()
    for i in range(0, len(player_hand[0])):
        counter = int(cards[0].index(player_hand[0][i]))
        player_hand[1].append(cards[1][counter])
    # print(player_hand[1])

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
        print(player_hand[1])
        if sum(player_hand[1]) > 21:
            print("Bust!")
            break
    elif play == "2":
        print("Stand")
        break