import re
text = input()
print(re.findall('[A-Z][^A-Z]*', text))