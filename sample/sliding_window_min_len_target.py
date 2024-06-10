nums=[2,3,1,2,4,3]
target=7
start=0
ml=float("inf")
ct=0
end=0
while(end<len(nums)):
    ct+=nums[end]
    while(ct>target):
        ct-=nums[start]
        start+=1
    if ct==target:
        print(end,start)
        ml=min(ml,end-start+1)
    end+=1
print(ml)