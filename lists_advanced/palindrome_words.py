strings = input().split()
palindrome_searched = input()
palindrome = []
for word in strings:
    if word == "".join(reversed(word)):
        palindrome.append(word)
print(f"{palindrome}")
print(f"Found palindrome {palindrome.count(palindrome_searched)} times")
