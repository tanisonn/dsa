nums=[1,2,3,4,1,2,3,1,2]
k=2
d={}
ans=0
start=-1
for end in range(0,len(nums)):
    d[nums[end]]=d.get(nums[end],0)+1
    while(d[nums[end]]>k):
        start+=1    
        ans=max(ans,end-start)
        d[nums[end]]-=1
print(ans)
