def foo(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

x = input()
print(foo(x))