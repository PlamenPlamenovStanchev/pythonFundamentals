n = int(input())
parking_database = {}

for _ in range(n):
    command, *args = input().split()

    if command == "register":
        username, license_plate = args[0], args[1]
        if username in parking_database:
            print(f"ERROR: already registered with plate number {parking_database[username]}")
        else:
            parking_database[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command == "unregister":
        username = args[0]
        if username not in parking_database:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_database[username]

for username, license_plate in parking_database.items():
    print(f"{username} => {license_plate}")
