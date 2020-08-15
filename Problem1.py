def solve(arr,goal):
    mp={}
    for num in arr:
        if goal-num in mp:
            print(num,goal-num)
            return
        mp[num]=1
    print("Doesn't Exist")
    return
        
#n=int(input())
arr=map(int,input().split())
goal=int(input())
solve(arr,goal)
