import re
m=input("enter a mac address")
n1="([0-9A-Fa-f]{2}\:){5}([0-9A-Fa-f])"
n2=re.findall(n1,m)
if re.search(n1,m):
    print("Valid",m)
else:
    print("Invalid",m)
