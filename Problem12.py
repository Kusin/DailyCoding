goal = int(input())
steps = list(map(int,input().split()))
steps.sort()
dp=[1]
for i in range(1,goal+1):
    ans=0
    for step in steps:
        if i-step<0:
            break
        ans+=dp[i-step]
    dp.append(ans)
print(dp[goal])