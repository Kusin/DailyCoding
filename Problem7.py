str=input()
DP=[1]
for i in range(len(str)) : DP.append(0)
for i,ch in enumerate(list(str),1):
    num=int(ch)
    if num>0:
        DP[i]+=DP[i-1]
    if i>1 and 1<=int(str[i-2:i])<=26 and str[i-2]!='0':
        DP[i]+=DP[i-2]
print(DP[len(str)])
