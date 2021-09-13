import re

a=input("enter a string")
b="ing$"
c=re.findall(b,a)
if len(a)==3:
    if len(c)==0:
        a=a+"ing"
    else:
        a=a+"ly"
else:
    print("string length is lessthen 3 eliments")
print(a)
