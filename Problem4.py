n=int(input())
arr=map(int,input().split())
arr=list([i for i in arr if i>0])
n=len(arr)
for i in arr:
    ind=i-1 if i>0 else -i-1
    if ind<n:
        if arr[ind]>0:
            arr[ind]*=-1
#if arr[x]<0 then x+1 exists in original array
ans=0
for i in range(n):
    if arr[i]>0:
        ans=i+1
        break
if not ans:
    ans=n+1
print(ans)
