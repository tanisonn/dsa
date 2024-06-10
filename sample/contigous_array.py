nums=[0,1,1]
M=[0]
count=0
ans=0
p=0
for i in range(len(nums)):
    if nums[i]==0:
        count+=-1
    else:
        count+=1
    M.append(count)

for j in range(1,len(M)):
    l=M[:j]
    print(l)
    if M[j] in l:
        p=l.index(M[j])
        print("TRUE",j)
        ans=max(ans,j-p)
print(ans)
    
            