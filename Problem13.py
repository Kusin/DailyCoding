def solve(k,string):
    if k<=0 or len(string)<=0:
        return (0,"")
    max_length=0
    ans_s=ans_e=-1
    s=e=0
    mp={string[0] : 1}
    while s<=e:
        if len(mp.keys())>k:
            mp[string[s]]=mp[string[s]]-1
            if mp[string[s]] == 0:
                del(mp[string[s]])
            s=s+1
        else:
            if e-s+1 > max_length:
                ans_s=s; ans_e=e
                max_length = e-s+1
            e=e+1
            if e==len(string): break
            if string[e] not in mp:
                mp[string[e]]=0
            mp[string[e]]=mp[string[e]]+1
    return (max_length,string[ans_s:ans_e+1])
            
k=int(input())
string=input()
print(solve(k,string))
    