import re

a="hii helllow hhhhhhhhhhhiiiiiiiiii"

b="[^hi..*]{1}"
b="h{2}.*"
#b="hi?"
b=".*"

c=re.findall(b,a)
print(c)