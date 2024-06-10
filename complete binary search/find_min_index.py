list_ele=[1,2,3,3,3,4,5,5,6,7]
target=3
l,h=0,len(list_ele)-1
while(l<=h):
    m=(l+h)//2
    if list_ele[m]<target:
        l=m+1
    else:
        h=m-1
print(l)