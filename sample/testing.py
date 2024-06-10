arr=[0,2,1,2,0]
n = len(arr)
stack=[]
left_smaller_indices = [-1] * n
for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if stack:
        left_smaller_indices[i] = stack[-1]
    stack.append(i)
    print(i,left_smaller_indices)
print(left_smaller_indices)