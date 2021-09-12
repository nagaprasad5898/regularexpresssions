#sub is a function in re module it will replace the old patteren with new
#in a given string
import re
a="123 hi frinds"
b=re.sub("123","hi",a)
print(b)
c=re.sub("hi","bye",a)
print(c)