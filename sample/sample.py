for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print("YES")
    else:
        a=str(a)
        b=str(b)
        if int(a[::-1])>int(b):
            print("Yes")
        elif(int(a[::-1])>int(b[::-1])):
            print("Yes")
        else:
            print("No")