import re

text = "apple banana cat dog"
pattern = r'\b[a-b]\w+'
result = re.findall(pattern, text)
print(result)