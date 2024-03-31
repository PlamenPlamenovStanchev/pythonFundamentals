# deck_of_cards = input().split()
# count_of_shuffles = int(input())
# deck_size = len(deck_of_cards)
# for current_shuffle in range(count_of_shuffles):
#     deck_after_shuffle = []
#     for i in range(deck_size // 2):
#         deck_after_shuffle.append(deck_of_cards[i])
#         deck_after_shuffle.append(deck_of_cards[i + deck_size // 2])
#     deck_of_cards = deck_after_shuffle
# print(deck_after_shuffle)



# deck_input = input().split()
# shuffles_count = int(input())
#
# Perform Faro shuffles
# deck_size = len(deck_input)
# for _ in range(shuffles_count):
#     shuffled_deck = []
#     for i in range(deck_size // 2):
#         shuffled_deck.append(deck_input[i])
#         shuffled_deck.append(deck_input[i + deck_size // 2])
#
#     deck_input = shuffled_deck
#
# Output: Print the state of the deck after the shuffles
# print(" ".join(deck_input))
# print(shuffled_deck)


deck_of_cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    deck_after_shuffing = []
    for index in range(len(left_part)):
        deck_after_shuffing.append(left_part[index])
        deck_after_shuffing.append(right_part[index])
    deck_of_cards = deck_after_shuffing
print(deck_of_cards)
