list_ele=[1,2,3,4,4,5,6,7]
target=4
l,h=0,len(list_ele)-1
k=None
while(l<=h):
    m=(l+h)//2
    if(list_ele[m]<=target):    
        l=m+1
    else:
        k=m
        h=m-1
print("The element bigger than target element is:",list_ele[k])