# capacity = int(input())
# users = {}
# while True:
#     command = input().split("=")
#     if command[0] == "Statistics":
#         break
#     if command[0] == "Add":
#         username = command[1]
#         sent = command[2]
#         received = command[3]
#         if username not in users:
#             users[username] = {"sent": sent,"received:": received}
#     elif command[0] == "Message":
#         sender = command[1]
#         receiver = command[2]
#         if sender in users and receiver in users:
#             users[sender]['sent'] += 1
#             users[receiver]['received'] += 1
#             if users[sender]['sent'] + users[sender]['received'] >= capacity:
#                 print(f"{sender} reached the capacity!")
#                 del users[sender]
#             if users[receiver]['sent'] + users[receiver]['received'] >= capacity:
#                 print(f"{receiver} reached the capacity!")
#                 del users[receiver]
#     elif command[0] == "Empty":
#         username = command[1]
#         if username == "All":
#             users.clear()
#         elif username in users:
#             del users[username]
# print(f"Users count: {len(users)}")
# for username, messages in sorted(users.items(), key=lambda x: (-x[1]['received'], x[0])):
#     print(f"{username} - {messages['sent'] + messages['received']}")


# capacity = int(input())
# users = {}
# while True:
#     command = input()
#     if command == "Statistics":
#        break
#     parts = command.split("=")
#     if len(parts) != 2:
#         continue
#     action = parts[0]
#     if action == "Add":
#         username = parts[1].split("=")[0]
#         sent = int(parts[1].split("=")[1])
#         received = int(parts[1].split("=")[2])
#         if username in users:
#             continue
#         users[username] = {"sent": sent,"received": received}
#     elif action == "Message":
#         sender = parts[1].split("=")[0]
#         receiver = parts[1].split("=")[1]
#         if sender not in users or receiver not in users:
#             continue
#         users[sender]["sent"] += 1
#         users[receiver]["received"] += 1
#         if users[sender]["sent"] >= capacity:
#             del users[sender]
#             print(sender + " reached the capacity!")
#     elif action == "Empty":
#         username = parts[1]
#         if username in users:
#             del users[username]
#         elif username == "All":
#             users.clear()
# print("Users count: " + str(len(users)))
# for user, data in sorted(users.items()):
#     print(user + " - " + str(data["sent"] + data["received"]))




# capacity = int(input())
# users = {}
# while True:
#     command = input().split("=")
#     if len(command) == 1 and command[0] == "Statistics":
#         break
#     action = command[0]
#     if action == "Add":
#         username, sent, received = command[1].split("{}=".format("{"))
#         sent, received = int(sent), int(received)
#         if username not in users:
#             users[username] = {"sent": sent, "received": received}
#
#     elif action == "Message":
#         sender, receiver = command[1].split("{}={}".format("{"))
#
#         if sender in users and receiver in users:
#             users[sender]["sent"] += 1
#             users[receiver]["received"] += 1
#
#             sent_total = users[sender]["sent"]
#             received_total = users[receiver]["received"]
#
#             if sent_total + users[sender]["received"] > capacity:
#                 print(f"{sender} reached the capacity!")
#             elif received_total + users[receiver]["sent"] > capacity:
#                 print(f"{receiver} reached the capacity!")
#
#     elif action == "Empty":
#         username = command[1]
#         if username == "All":
#             users.clear()
#         elif username in users:
#             del users[username]
#
# print("Users count: " + str(len(users)))
# for user, data in sorted(users.items()):
#     print(user + " - " + str(data["sent"] + data["received"]))


# def add_user(users, username, sent, received):
#     if username not in users:
#         users[username] = {"sent": sent, "received": received}
#
# def send_message(users, sender, receiver, capacity):
#     if sender in users and receiver in users:
#         users[sender]["sent"] += 1
#         users[receiver]["received"] += 1
#
#         if users[sender]["sent"] >= capacity:
#             print(f"{sender} reached the capacity!")
#             del users[sender]
#         if users[receiver]["received"] >= capacity:
#             print(f"{receiver} reached the capacity!")
#             del users[receiver]
#
# def empty_user(users, username):
#     if username == "All":
#         users.clear()
#     elif username in users:
#         del users[username]
#
# def print_statistics(users):
#     print(f"Users count: {len(users)}")
#     for username, info in sorted(users.items(), key=lambda x: (-x[1]["received"], x[0])):
#         total_messages = info["sent"] + info["received"]
#         print(f"{username} - {total_messages}")
#
# def message_management():
#     capacity = int(input())
#     users = {}
#
#     while True:
#         command = input().split("=")
#         if command[0] == "Statistics":
#             break
#
#         if command[0] == "Add":
#             username = command[1]
#             sent = int(command[2])
#             received = int(command[3])
#             add_user(users, username, sent, received)
#
#         elif command[0] == "Message":
#             sender = command[1]
#             receiver = command[2]
#             send_message(users, sender, receiver, capacity)
#
#         elif command[0] == "Empty":
#             username = command[1]
#             empty_user(users, username)
#
#     print_statistics(users)
#
# message_management()

messages_capacity = int(input())
command = input().split('=')
records = {}
while command[0] != 'Statistics':
    command = command[0]
    if command == 'Add':
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username in records:
            command = input().split('=')
            continue
        records[username] = []
        records[username].append(sent)
        records[username].append(received)
    elif command == 'Message':
        sender = command[1]
        receiver = command[2]
        if sender in records and receiver in records:

            records[sender][0] += 1
            if records[sender][0] + records[sender][1] >= messages_capacity:
                del records[sender]
                print(f"{sender} reached the capacity!")

            records[receiver][1] += 1

            if records[receiver][1] + records[receiver][0] >= messages_capacity:
                del records[receiver]
                print(f"{receiver} reached the capacity!")
    elif command == 'Empty':
        username = command[1]
        if username == 'All':
            records = {}
        else:
            del records[username]
    command = input().split('=')
print(f'Users count: {len(records)}')
for username, info in sorted(records.items(), key=lambda i: (-i[1][1], i[0])):
    print(f'{username} - {sum(info)}')