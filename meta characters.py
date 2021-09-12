#to match the patteren starting use '^' in front of patteren and for end '$' at end
#to serch unknow '.' use this characters
#for '*' it will allow all charcters for 0 or n times excpt newline
# '+' it will allow 1 or more times
# '?' it will allow 0 or 1 time
#letsee with examples
import re
a="hi frinds i am nagaprasad"
b=re.findall(".i",a) # '.'it will allow any charter infront of the string
print(b)
c=re.findall(".",a)
print(c)
d=re.findall("i.",a)
print(d)
e=re.findall("....",a)
print(e)
#"*"
f=re.findall("i*",a)
print(f)
#g=re.findall("*i",a)# "*" must give before the charcter
#print(g)
h=re.findall("^h.*",a)
print(h)
i=re.findall("h.+",a)#it will allow the character 1 or more times
print(i)
j=re.findall("z+",a)
print(j)
