#[] we can place patteren in that and {} in this we will place no of times to repeted
import re

a="python is a simplest language"
b=re.findall("[a]{1}",a)
print(b)
c=re.findall("[a-z ]{5}",a)
print(c)
e="i am engnr and my rollno was 136"
d=re.findall("[a-zA-Z1-9]{2}",a)
print(d)