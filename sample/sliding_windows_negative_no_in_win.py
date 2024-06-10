a=[1,2,-3,4,-3,-1,4,-5,1,2,3]
k=3
neg=[]
ans=[]
for i,num in enumerate(a):
    # initally while iterating we ll add the negative vlues into the neg list so that we dnt need to check again
    if num<0:
        neg.append(i)
    # we omit the neg elements once the window is crossed that pointer
    if len(neg)>0 and i-neg[0]==k :
        neg.pop(0)
    # The first element in the neg array carries the first negative no in the array if there are no element we return 0
        # initally we start that condtion once the start pointer completes once window
    if i>=k-1:
        if len(neg)>0:
            ans.append(a[neg[0]])
        else:
            ans.append(0)
print(ans)


    