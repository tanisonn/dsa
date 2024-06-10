list_ele=[1,2,3,4,4,4,5,6,7]
target=4
l,h=0,len(list_ele)-1
k=None
while(l<=h):
    m=l+(h-l)//2
    #m=(l+h)//2
    if(list_ele[m]<target):
        key=m
        l=m+1
    else:
        h=m-1
print("The element less than target element is:",list_ele[l])