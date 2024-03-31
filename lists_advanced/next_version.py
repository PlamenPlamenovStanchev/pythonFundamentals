current_version = input()
version_number = list(map(int, current_version.split(".")))
version_number[-1] += 1
for i in range(len(version_number)-1, 0, -1):
    if version_number[i] > 9:
        version_number[i] = 0
        version_number[i-1] += 1
    else:
        break
next_version = ".".join(map(str, version_number))
print(next_version)
