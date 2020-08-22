path = input()
newline ='\\n'; tab = '\\t'
elements = path.split(newline)
dt = []
answer = 0
for elem in elements:
    tab_cnt = elem.count(tab)
    length = len(elem) - 2*tab_cnt #eliminating count of tab
    if tab_cnt > 0:
        length+=1 #path contains / if it is not the root
    if len(dt) == tab_cnt:
        dt.append(length)
    else:
        dt[tab_cnt] = length
    if tab_cnt > 0:
        dt[tab_cnt] += dt[tab_cnt-1]
    if '.' in elem: #if elem is a file
        answer = max(answer,dt[tab_cnt])
print(answer)