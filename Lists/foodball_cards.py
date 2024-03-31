# cards_input = input()
#
# team_a_players = list(range(1, 12))
# team_b_players = list(range(1, 12))
#
# for card in cards_input:
#     team, player = card.split('-')
#     player = int(player)
#
#     if team == 'A' and player in team_a_players:
#         team_a_players.remove(player)
#     elif team == 'B' and player in team_b_players:
#         team_b_players.remove(player)
#
#     if len(team_a_players) < 7 or len(team_b_players) < 7:
#         print("Game was terminated")
#         break
# else:
#     print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")#
#




# def process_cards(card_sequence):
#     team_a_players = list(range(1, 12))
#     team_b_players = list(range(1, 12))
#
#     for card in card_sequence:
#         team, player = card.split('-')
#         player = int(player)
#
#         if team == 'A' and player in team_a_players:
#             team_a_players.remove(player)
#         elif team == 'B' and player in team_b_players:
#             team_b_players.remove(player)
#
#         if len(team_a_players) < 7 or len(team_b_players) < 7:
#             print("Game was terminated")
#             return
#
#     print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
#
# Input: Receive a sequence of cards separated by a single space
# cards_input = input().split()

# Output: Process the cards and print the remaining players on each team
# process_cards(cards_input)





team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", 'A-7', "A-8", 'A-9', 'A-10', "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
players = input().split()
game_was_terminated = False
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")