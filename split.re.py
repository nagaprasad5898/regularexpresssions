import re
#split is also a re function it takes input as patteren,string and no of times to split
# if we dont provide anythng it defalutly take it has count of the patteren

a="hi frnds how are u all"
b=re.split(" ",a,2)
c=re.split("h",a)
print("b string split with space:",b)
print("c string split with h:",c)
print(" ".join(b))
for i in b:
    print(i)
for i in c:
    print(i)