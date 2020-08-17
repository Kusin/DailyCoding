'''
if you want to graph the points,
uncomment the plt codes
'''
import random
import time
#from matplotlib import pyplot as plt
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed
@timeit
def main(**kwargs):
    r = 1.0
    total = int(5e6)
    count = 0
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim(-r,r)
    plt.ylim(-r,r)
    '''
    for times in range(1,total+1):
        x=random.uniform(-r,r); y=random.uniform(-r,r)
        if x*x+y*y<=r*r:
            count+=1
            #plt.scatter(x,y,c='r',marker='.')
        else:
            None
            #plt.scatter(x,y,c='b',marker='.')
        probablity = count / times
        pi = round(probablity * 4, 20)
        '''
        plt.pause(1e-8)
        plt.title(r'$\pi$ = %s' %pi)
        plt.draw()
        '''
    print(pi)
logtime_data={}
f=open("log.txt","w")
main(log_time=logtime_data)
f.write(str(logtime_data))
f.close()

