import re

txt = input()
x = r'ab{2,3}'
pt = re.search(x, txt)
if pt is not None:
    print(pt)
else:
    print('qate')
