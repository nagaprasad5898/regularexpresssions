import re
a=input("enter an email:")
try:
    b=re.search(r"(\w+)(@)(\w+)(.\w{2,3})",a)
    print(b.group(1))
    print(b.group(3))
except AttributeError:
    print("wrong input")