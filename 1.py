import re

txt = input()
x = r'ab*'
pt = re.search(x, txt)
if pt is not None:
    print(pt)
else:
    print('qate')
