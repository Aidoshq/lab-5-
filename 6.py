import re
text = input()
print(re.sub("[ ,.]", ":", text))