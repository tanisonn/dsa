arr=[1,2,3,4,1,2,5]
win_size=3
#to find the max sum of subarray whose size is win_size
su=0
start=0
end=0
ma=float("-inf")
"""while(end<len(arr)):
    if(end-start+1<=win_size):
        su+=arr[end]
        end+=1
    else:
        ma=max(ma,su)
        su-=arr[start]
        start+=1
        su+=arr[end]
        end+=1
else:
    ma=max(ma,su)"""
for i in range(win_size):
    su+=arr[i]
ma=su
for end in range(win_size,len(arr)):
    su-=arr[start]
    start+=1
    su+=arr[end]
    ma=max(ma,su)
print(ma)


        
    