nums=[-3,-2,-1,0,0,1,2]
l,r=0,len(nums)-1
pos=0
neg=0
while(l<=r):
    m=(l+r)//2
    if(nums[m]<1):
        l=m+1
    else:
        if(m==0 or nums[m-1]<1):
            pos= m
            break
        else:
            r=m-1
else:
    pos=len(nums)
p,q=0,len(nums)-1
while(p<=q):
    m=(p+q)//2
    if(nums[m]>=0):
        q=m-1
    else:
        if m==len(nums)-1 or nums[m+1]>=0:
            neg= m
            break
        else:
            p=m+1
else:
    neg=-1
print((neg+1,len(nums)-pos))
