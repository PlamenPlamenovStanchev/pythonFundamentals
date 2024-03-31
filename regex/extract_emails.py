# import re
# string = input()
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# matches = re.findall(regex, string)
# for email in matches:
#     print(email)

import re
sentence = input()
pattern = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
extracted_emails = re.findall(pattern, sentence)
for email in extracted_emails:
    print(email[0])
