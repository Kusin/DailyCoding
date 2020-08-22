from collections import deque
array =[int(i) for i in input().strip().split()]
k = int(input())
dq = deque()
ans=[]
for index,element in enumerate(array):
    while dq and dq[-1] < element:
        dq.pop()
    dq.append(element)
    if index>=k and dq[0] == array[index-k]:
        dq.popleft()
    if index >= k-1: # when window's size reached k
        ans.append(dq[0])
print(*ans)