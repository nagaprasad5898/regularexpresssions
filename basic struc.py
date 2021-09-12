import re
#we have lot of functions in re but mainly we use 4functions
#1st search
a="kanna is gud boy"
c=re.search("(^ka)(\w+)",a)
print(c)
print(c.group(0))
print(c.group(1))
print(c.group(2))
d= re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')
print(d)
print(d.group())
print(d.group(1))
print(d.group(2))
print(d.group(3))