#n=int(input())
arr=list(map(int,input().split()))
INF = 1e9
DP1=arr[0]; DP2=-INF
for i in range(1,len(arr)):
    a=max(DP2,0)+arr[i]
    b=max(DP1,DP2)
    DP1=a
    DP2=b
print(max(DP1,DP2))
