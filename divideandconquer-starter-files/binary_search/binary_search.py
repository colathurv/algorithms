# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array
import math


isFirstRow  = True
not_done = True
A = []
S = []
n = 0 
k = 0
output = []


def BinarySearch(A, low, high, key):
    #print '---------------------'
    #print 'Calling BinarySearch'
    #print 'low = %d' % low
    #print 'high = %d' % high
    #print 'key = %d' % key
    
   
    if high < low:
        return -1
    mid = low + int(math.floor((high - low)/2))
    #print 'mid = %d' % mid
    
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return BinarySearch(A, low, mid - 1, key)
    else:
        return BinarySearch(A, mid + 1, high, key)

while not_done:
    line = sys.stdin.readline().rstrip('\n')
    if isFirstRow:
        line = line.split()    
        n = int(line[0])
        for i in range(n):
            A.insert(i,int(line[i + 1]))
        isFirstRow = False 
    else:
        line = line.split()
        k = int(line[0])
	for i in range(k):
            S.insert(i,int(line[i + 1]))
        not_done = False
        
#print A
#print n
#print S
#print k

for i in range(k):
      x = BinarySearch(A, 0, n-1, S[i])
      output.append(x)

#print output
print ' '.join(map(str, output))