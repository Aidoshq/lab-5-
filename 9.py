import re
def foo(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

x = input()
print(foo(x))
