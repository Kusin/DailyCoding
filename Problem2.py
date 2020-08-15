import copy
def make_prefix(arr):
    num=1
    prefix=[1]
    for k in arr:
        num*=k
        prefix.append(num)
    prefix.append(1)
    return prefix
        
def make_suffix(arr):
    rarr=reversed(arr)
    num=1
    suffix=[1]
    for k in rarr:
        num*=k
        suffix.append(num)
    suffix.append(1)
    suffix.reverse()
    return suffix
    
#n=int(input())
arr=list(map(int,input().split())); n=len(arr)
pre=make_prefix(arr); suf=make_suffix(arr)
answer=[ pre[i-1] * suf[i+1] for i in range(1,n+1)]
print(answer)

