import re
a=input("enter passdword:")
c=re.findall("[0-9]+|[A-Z]+|[a-z]+|[@#$]+",a)
if len(c)==4 and 6<=len("".join(c))<=12:
    if "".join(c)==a:
        print("".join(c))
    else:
        print("wrong pattern")
else:
    print("wrng pattern")

