def solve(row:int=0, state:int=0, weight:int=0) ->int:
    global dp,n,k
    if state in dp and weight >= dp[state] or row>n:
        return
    dp[state] = weight
    for col in range(k):
        if not state & 1<<col:
            solve(row+1,state | 1<<col,weight+arr[row][col])    
n,k = [int(i) for i in input().strip().split()]
arr = [[int(i) for i in input().strip().split()] for _ in range(n)]
dp={}
solve()
final_state = (1<<n) -1
print(dp[final_state])