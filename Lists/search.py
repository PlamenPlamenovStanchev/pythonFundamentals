number = int(input())
word = input()
string = []
for current_number in range(number):
    current_string = input()
    string.append(current_string)
print(string)
for current_word in range(len(string)-1, -1, -1):
    element = string[current_word]
    if word not in element:
        string.remove(element)
print(string)