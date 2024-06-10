def test(z):
    l=['9', '99', '999', '9999', '99999', '999999', '9999999', '99999999', '999999999', '9999999999', '99999999999', '9999999999999999','999999999999', '9999999999999', '99999999999999', '999999999999999', '9999999999999999', '99999999999999999', '999999999999999999', '9999999999999999999',]
    m=len(z)
    if m>1 :
        """if m==2:
            z=str(int(z)+1)
            for i in range(11):
                if str(z)!=str(z)[::-1]:
                    z=str(int(z)+1)
                else:
                    break
            print(z)"""
        if m>1:

            if z==z[::-1]:
                if z in l:
                    return (int(z)+2)
                else:
                    if m&1:
                        if z[m//2]!="9":
                            return (z[:m//2]+str(int(z[m//2])+1)+z[m//2+1:])
                        else:
                            k=int(z[:m//2+1])
                            k=k+1
                            k=str(k)
                            p=k[:len(k)-1]
                            return (k+p[::-1])
                    else:
                        k=int(z[:m//2])
                        k=k+1
                        k=str(k)
                        p=k[:len(k)]
                        return (k+p[::-1])
            else:
                if m&1:
                    f=int(z[:m//2][::-1])
                    s=int(z[m//2+1:])
                    if f<s:
                        k=int(z[:m//2+1])
                        k=k+1
                        k=str(k)
                        p=k[:len(k)-1]
                        return (k+p[::-1])
                    else:
                        return (str(f)[::-1]+str(z[m//2])+str(f))
                else:
                    f=int(z[:m//2][::-1])
                    s=int(z[m//2:])
                    if f<s:         
                        k=int(z[:m//2])
                        k=k+1
                        k=str(k)
                        p=k[:len(k)]
                        return (k+p[::-1])
                    else:
                        return (str(f)[::-1]+str(f))
    else:
        if z=="9":
             return ("11")
        else:
            return (int(z)+1)
def train(z):
    a=int(z)
    a+=1
    while not str(a)==str(a)[::-1]:
        a+=1
    return (a)
print(test("1000"))
"""for i in range(10000):
    if str(train(str(i)))!=str(test(str(i))):
        print("not",i)
else:
    print("comp")"""


