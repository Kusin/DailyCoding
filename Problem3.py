class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
spliter='/'
null='NIL'
def serialize(root):
    if not root or not root.val:
        return null+spliter
    s=root.val+spliter
    rval=lval=''
    if root.left:
        lval=root.left.val+spliter
    else:
        lval=null+spliter
    if root.right:
        rval=root.right.val+spliter
    else:
        rval=null+spliter
    s+=lval+rval
    if root.left:
        s+=serialize(root.left)
    if root.right:
        s+=serialize(root.right)
    return s;
def dfs(L):
    if not L:
        return None
    val=L[-1]; L.pop()
    lval=L[-1]; L.pop()
    rval=L[-1]; L.pop()
    if lval==null:
        lval=None
    if rval==null:
        rval=None
    lnode=None; rnode=None
    if lval:
        lnode=dfs(L)
    if rval:
        rnode=dfs(L)
    return Node(val,lnode,rnode)
def deserialize(s):
    L=s.split(spliter)
    if len(L)<=2:
        return None
    L.pop() #eliminate the last space
    L.reverse()
    return dfs(L)

if __name__=="__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    
