# number_of_rooms = int(input())
# free_chairs = 0
# for room_number in range(1, number_of_rooms + 1):
#     room_info = input()
#     chairs, visitors = room_info.split()
#     chairs_needed = max(0, int(visitors) - len(chairs))
#     if chairs_needed > 0:
#         print(f"{chairs_needed} more chairs needed in room {room_number}")
#     else:
#         free_chairs += len(chairs) - int(visitors)
# if free_chairs >= 0:
#     print(f"Game On, {free_chairs} free chairs left")


def check_the_room(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms+1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs
count_of_room = int(input())
total_free_chairs = check_the_room(count_of_room)
if total_free_chairs >=0:
    print(f"Game On, {total_free_chairs} free chairs left")



