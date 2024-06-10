a=[1,2,3,4,4,21,91]
b=[3,5,7,22,91,92]
ans=[]
i=0
j=0
while (i<len(a) and j<len(b)):
    if(a[i]<=b[j]):
        ans.append(a[i])
        i+=1
    else:
        ans.append(b[j])
        j+=1
while i<len(a):
    ans.append(a[i])
    i+=1
while j<len(b):
    ans.append(b[j])
    j+=1
print(ans)
    

