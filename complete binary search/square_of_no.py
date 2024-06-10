c=10
l=0
h=int(c**0.5)
while(l<=h):
    su=l*l+h*h
    if su==c:
        print(True)
        break
    elif su>c:
        h-=1
    else:
        l+=1
else:
    print(False)