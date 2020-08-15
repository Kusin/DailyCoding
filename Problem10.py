import time
def f():
    print('surprise!')
def scheduler(func,t):
    start=time.time()
    while (time.time()-start)*1e3<t:None
    f()
def main():
    n=int(input())
    scheduler(f,n)
main()