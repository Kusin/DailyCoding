from collections import deque
class logStorage:
    def __init__(self,n=100):
        self.N = n
        self.dq = deque()
    def record(self,order_id):
        '''
        records information
        @param : order info
        @return : void
        '''
        self.dq.append(order_id)
        if len(self.dq)>self.N:
            self.dq.popleft()
    def get_last(self,i):
        '''
        @param : index smaller than N
        @return : ith last element from the log
        '''
        return self.dq[-1]
#n=int(input())
n=2
LS = logStorage(n)
sample_order = ['Kim', 'James','Hello','Penta']
for ord in sample_order:
    LS.record(ord)
    print(f"the last element is {LS.get_last(1)}")
