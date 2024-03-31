def processed_submission(submissions, bans, number_of_submissions, username, language, points):
    if language not in number_of_submissions:
        number_of_submissions[language] = 1
    else:
        number_of_submissions[language] += 1

    if username not in bans:
        if username in submissions:
            if language in submissions[username]:
                submissions[username][language] = max(submissions[username][language], points)
            else:
                submissions[username][language] = points
        else:
            submissions[username] = {'language': points}

def print_results(submissions):
    print("Results:")
    for username, language in submissions.items():
        max_points = max(language.values())
        print(f"{username} | {max_points}")

def print_submissions(number_of_submissions):
    print("Submissions:")
    for language, count in number_of_submissions.items():
        print(f"{language} - {count}")

submissions = {}
bans = []
number_of_submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break
    tokens = command.split('-')
    if len(tokens) == 3:
        username, language, points = tokens
        points = int(points)
        processed_submission(submissions, bans, number_of_submissions, username, language, points)
    elif len(tokens) == 2:
        username, actions = tokens
        if actions == "banned":
            bans.append(username)


for username in bans:
    if username in submissions:
        del submissions[username]

print_results(submissions)
print_submissions(number_of_submissions)