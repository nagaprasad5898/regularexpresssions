#"^" if we place this symbol at the strt of the serch pattern it will serch at strt of the string
#if we "$" at the end of the pattern it will serch at the end
#in this we are using find function from re
#findall will return [] if the given patteren was not in that string else it eill return with the
# patteren provided as shown in below example

import re
a="hi we are from vijayawada"
c=re.findall("da$",a)
print("it will check if the given patteren is in end or not:",c)
d=re.findall("^hi",a)
print("it will check given patteren is in 1st place or not:",d)
e=re.findall("hi$",a)
print("it will check if the given patteren is in end or not:",e)
f=re.findall("^vijayawada",a)
print("it will check if the given patteren is in 1st or not:",f)
