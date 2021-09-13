import re
a=input("enter an string:")
b="[0-9]+"
c=re.findall(b,a)
print(c)
print(",".join(c))
