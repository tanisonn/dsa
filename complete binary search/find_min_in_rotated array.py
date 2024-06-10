arr=[17,21,43,-1,0,0]
l,r=0,len(arr)-1
while(l<r):
    m=(l+r)//2
    if arr[m]<arr[r]:
        r=m
    elif arr[m]>arr[r]:
        l=m+1
    else:
        r-=1
print(arr[l])
