# using bisect
# O(nm log n) preprocess
# O(m log n) search
import bisect
def startsWith(prefix,strings):
    strings =sorted([string.lower() for string in strings])
    nextstr=prefix[:-1]+chr(ord(prefix[-1])+1)
    return strings[bisect.bisect_left(strings,prefix):bisect.bisect_left(strings,nextstr)]
strings = ['dog', 'deer', 'deal' , 'ddong','de']
prefix = 'de'
print(startsWith(prefix,strings))